from persons.models import Person


class VPNParser:
    """
    Class that reads logs of the VPN and stores it in the database.
    """

    @staticmethod
    def __get_user(user_login):
        """
        Gets the user from the database.

        Returns
        -------
        int
            an int that identifies a person
        """
        identifier = None
        try:
            identifier = Person.objects.get(login=user_login).id
        except DoesNotExist:
            print(f'User not found for login {user_login}!')
        finally:
            return identifier

    @staticmethod
    def load_data():  # TODO
        """
        Loads the VPN XML log in memory.

        Returns
        -------
        ndarray
            an array with the event, app (Windows OS), person id, item id and timestamps
        """

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
