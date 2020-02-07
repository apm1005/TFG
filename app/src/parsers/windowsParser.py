import os
import numpy as np
import locale
import datetime
from logscope.models import Person, Eventtype, Event, App, Passage


class LanguageNotSupported(Exception):
    """
    Raised when the language of Windows is not Spanish or English
    """

    def __init__(self, message):
        self.message = message


class WindowsParser:
    """
    Class that executes a command in Windows to extract the last login of the users
    """

    @staticmethod
    def __get_users():
        """
        Gets the users from the database

        Returns
        -------
        ndarray
            an array with the id and login of each person
        """
        return np.array(Person.objects.values_list('id', 'login'), dtype='object')

    @staticmethod
    def __set_logon_string():
        """
        Sets the string that will be used in the cmd command to look for last logon

        Raises
        ------
        LanguageNotSupported
            if the OS language is not considered

        Returns
        -------
        string
            an string with the info to look for last logon
        """
        language = locale.getdefaultlocale()[0]

        if language == 'es_ES':
            logon_string = 'Ultima'
        elif language == 'en_US':
            logon_string = 'Last logon'
        else:
            raise LanguageNotSupported('The current Windows language is not supported!')

        return logon_string

    def __load_data(self):
        """
        Loads the last login of each person in memory

        Returns
        -------
        ndarray
            an array with the person id, user login and timestamps
        """
        users = self.__get_users()
        logons = np.empty((users.shape[0], 1), dtype=object)
        result = np.hstack((users, logons))
        date_length = 22
        logon_string = self.__set_logon_string()

        for i, user in enumerate(result):
            user_id, user_login, _ = user
            command = f'net user {user_login} | findstr /B /C:"{logon_string}"'
            timestamp_logon = str(os.popen(command).read())
            if timestamp_logon != '':
                parsed_timestamp = self.__parse_timestamp(
                    timestamp_logon[-date_length:].replace('?', '').replace('\n', ''))
                result[i, 2] = parsed_timestamp

        return result

    @staticmethod
    def __parse_timestamp(timestamp):
        """
        Parses the timestamp given to a format that the ORM can store

        Parameters
        ----------
        timestamp : timestamp
            user last logon timestamp

        Returns
        -------
        timestamp
            user last logon timestamp parsed
        """
        units = datetime.datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S')
        return datetime.datetime.strftime(units, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __create_event(user_last_logon):
        """
        Creates an Event in the database

        Parameters
        ----------
        user_last_logon : timestamp
            user last logon timestamp

        Returns
        -------
        int
            identifier for the event created
        """
        type_of_event = Eventtype.objects.get(type='log in')
        event = Event.objects.create(instant=user_last_logon, event_type=type_of_event)
        event.save()
        return event.id

    @staticmethod
    def __create_passage(user_id, user_last_logon, event_id):
        """
        Creates a Passage in the database

        Parameters
        ----------
        user_id : int
            user identifier
        user_last_logon : timestamp
            user last logon timestamp
        event_id : int
            event identifier
        """
        Passage.objects.create(start_time=user_last_logon,
                               end_time=None,
                               app_id=App.objects.get(name='Windows').id,
                               event_id=event_id,
                               item_id=None,
                               person_id=user_id)

    @staticmethod
    def __check_if_exists(user_id, user_last_logon):
        """
        Checks if a logon is already in the database

        Parameters
        ----------
        user_id : int
            user identifier
        user_last_logon : timestamp
            user last logon timestamp

        Returns
        -------
        boolean
            True if the logon is already in the database
            False if the logon is not in the database
        """
        exists = None
        try:
            Passage.objects.get(person_id=user_id,
                                start_time=user_last_logon,
                                app_id=App.objects.get(name='Windows').id)
            exists = True
        except DoesNotExist:
            exists = False
        finally:
            return exists

    def __store_data(self):
        """
        Stores the data into the Event entity and Passage entity
        """
        users = self.__load_data()

        for i, user in enumerate(users):
            user_id, user_login, user_last_logon = user
            if user_last_logon is not None and not self.__check_if_exists(user_id=user_id,
                                                                          user_last_logon=user_last_logon):
                event_id = self.__create_event(user_last_logon=user_last_logon)
                self.__create_passage(user_id=user_id, user_last_logon=user_last_logon, event_id=event_id)

    def parse(self):
        """
        Parses the login of each person from Windows and stores it in the database
        """
        self.__store_data()
