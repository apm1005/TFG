import os
import numpy as np
from persons.models import Person


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

        for i, user in enumerate(result):
            command = f'net user {user[1]} | findstr /B /C:"Ultima sesión iniciada"'
            r = str(os.popen(command).read())
            if r != '':
                result[i, 2] = r[-22:].replace('?', '').replace('\n', '')

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
