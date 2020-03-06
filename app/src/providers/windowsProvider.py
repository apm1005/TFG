from .provider import Provider
from tfgproject.settings import LOGON_CUT_STRING
from logscope.models import (
    App,
    Eventtype,
    Person,
)
import os
import numpy as np
import locale
import ctypes
import datetime


class LanguageNotSupported(Exception):
    """
    Raised when the language of Windows is not Spanish or English
    """

    def __init__(self, message):
        self.message = message


class WindowsProvider(Provider):
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
        windll = ctypes.windll.kernel32
        language = locale.windows_locale[windll.GetUserDefaultUILanguage()]

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
        logon_string = self.__set_logon_string()

        for i, user in enumerate(result):
            user_id, user_login, _ = user
            command = f'net user {user_login} | findstr /B /C:"{logon_string}"'
            timestamp_logon = str(os.popen(command).read())
            if timestamp_logon != '':
                parsed_timestamp = self._parse_timestamp(
                    timestamp_logon[-LOGON_CUT_STRING:].replace('?', '').replace('\n', ''))
                result[i, 2] = parsed_timestamp

        return result

    def _parse_timestamp(self, timestamp):
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

    def store_data(self):
        """
        Stores the data into the Event entity and Passage entity
        """
        users = self.__load_data()

        for i, user in enumerate(users):
            user_id, user_login, user_last_logon = user
            if user_last_logon is not None \
                    and not super()._check_if_passage_exists(instant=user_last_logon,
                                                             user_id=user_id,
                                                             app_id=App.objects.get(name='Windows').id):
                event_id = super()._create_event(instant=user_last_logon,
                                                 end_time=None,
                                                 event_type=Eventtype.objects.get(type='log in'))
                super()._create_passage(instant=user_last_logon,
                                        end_time=None,
                                        app_id=App.objects.get(name='Windows').id,
                                        event_id=event_id,
                                        item_id=None,
                                        user_id=user_id)
