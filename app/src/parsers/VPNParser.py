import numpy as np


class VPNParser:
    """
    Class that reads logs of the VPN and stores it in the database.
    """

    def __get_users(self):  # TODO
        """
        Gets the users from the database.

        Returns
        -------
        list
            a list with the login of each person
        """
        pass

    def __load_data(self):  # TODO
        """
        Loads the last login of each person in memory.

        Returns
        -------
        ndarray
            an array with the event, app (Windows OS), person id, item id and timestamps
        """
        pass

    def __store_data(self):  # TODO
        """
        Stores the data into the Event entity and Passage entity.
        """
        pass

    def parse(self):  # TODO
        """
        Parses the events of the VPN and stores them in the database.
        """
        pass
