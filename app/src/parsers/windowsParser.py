import os
import numpy as np
import locale
from persons.models import Person


class LanguageNotSupported(Exception):
    """
    Raised when the language of Windows is not Spanish or English
    """

    def __init__(self, message):
        self.message = message


class WindowsParser:
    """
    Class that executes a command in Windows to extract the last login of the users.
    """

    def __get_users(self):
        """
        Gets the users from the database.

        Returns
        -------
        ndarray
            an array with the id and login of each person
        """
        return np.array(Person.objects.values_list('id', 'login'), dtype='object')

    def __load_data(self):  # TODO
        """
        Loads the last login of each person in memory.

        Returns
        -------
        ndarray
            an array with the event, app (Windows OS), person id, item id and timestamps
        """
        users = self.__get_users()
        logons = np.empty((users.shape[0], 1), dtype=object)
        result = np.hstack((users, logons))
        date_length = 22
        language = locale.getdefaultlocale()[0]

        if language == 'es_ES':
            logon_string = 'Ultima'
        elif language == 'en_US':
            logon_string = 'Last logon'
        else:
            raise LanguageNotSupported('The current Windows language is not supported!')

        for i, user in enumerate(result):
            user_id, user_login, _ = user
            command = f'net user {user_login} | findstr /B /C:"{logon_string}"'
            timestamp_logon = str(os.popen(command).read())
            if timestamp_logon != '':
                result[i, 2] = timestamp_logon[-date_length:].replace('?', '').replace('\n', '')

        return result

    def __store_data(self):  # TODO
        """
        Stores the data into the Event entity and Passage entity.
        """
        pass

    def parse(self):  # TODO
        """
        Parses the login of each person from Windows and stores it in the database.
        """
        return self.__load_data()
