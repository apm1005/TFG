from .provider import Provider
from logscope.models import (
    App,
    Item,
    Passage,
    Person,
)
from .xmlFileManager import XMLFileManager
import datetime
import locale


class VPNProvider(Provider):
    """
    Class that reads logs of the VPN and stores it in the database.
    """

    def __init__(self):
        self.__file_manager = XMLFileManager()

    @staticmethod
    def __get_user(user_login):
        """
        Gets the user from the database

        Parameters
        ----------
        user_login : str
            person login

        Returns
        -------
        int
            an int that identifies a person
        """
        if '@' in user_login:
            user_login = str(user_login).split('@')[0]
        elif '\\\\' in user_login:
            user_login = str(user_login).split('\\\\')[1]

        identifier = None
        try:
            identifier = Person.objects.get(login=user_login).id
        except DoesNotExist:
            print(f'User not found for login {user_login}!')
        finally:
            return identifier

    @staticmethod
    def __parse_event_type(event_message):
        """
        Parses the type of event read in the XML file

        Parameters
        ----------
        event_message : str
            message with the type of event

        Returns
        -------
        str
            string with the event in a format that the ORM can store
        """
        event_type = None
        if 'login' in event_message:
            event_type = 'log in'
        elif 'logged out' in event_message:
            event_type = 'log out'
        return event_type

    @staticmethod
    def __set_start_time(instant, duration):
        """
        Reads the timestamp given and checks if it necessary to create another timestamp based
        on the duration parameter

        Parameters
        ----------
        instant : timestamp
            timestamp of event
        duration : str
            string with the time of the VPN connection

        Returns
        -------
        timestamp
            new timestamp for the passage
        """
        start_time = None
        if duration != 'N/A':
            units_instant = datetime.datetime.strptime(instant, '%Y-%m-%d %H:%M:%S')
            instant_time = datetime.timedelta(hours=units_instant.hour,
                                              minutes=units_instant.minute,
                                              seconds=units_instant.second)
            units_duration = datetime.datetime.strptime(duration, '%H:%M:%S')
            duration_time = datetime.timedelta(hours=units_duration.hour,
                                               minutes=units_duration.minute,
                                               seconds=units_duration.second)
            new_time = instant_time - duration_time
            units_new_time = datetime.datetime.strptime(str(new_time), '%H:%M:%S')
            start_time = datetime.datetime.strftime(
                datetime.datetime(year=units_instant.year,
                                  month=units_instant.month,
                                  day=units_instant.day,
                                  hour=units_new_time.hour,
                                  minute=units_new_time.minute,
                                  second=units_new_time.second), '%Y-%m-%d %H:%M:%S')
        return start_time

    @staticmethod
    def __get_item(ip_address):
        """
        Gets the item from the database

        Parameters
        ----------
        ip_address : str
            ip address of the item used

        Returns
        -------
        int
            an int that identifies an item
        """
        identifier = None
        try:
            identifier = Item.objects.get(ip_address=ip_address).id
        except DoesNotExist:
            print(f'IP not found {ip_address}!')
        finally:
            return identifier

    @staticmethod
    def __get_app(app):
        """
        Gets the app from the database

        Parameters
        ----------
        app : str
            app of the parser

        Returns
        -------
        int
            an int that identifies an app
        """
        identifier = None
        try:
            identifier = App.objects.get(name=app).id
        except DoesNotExist:
            print(f'App {app} not found!')
        finally:
            return identifier

    @staticmethod
    def __update_passage(instant, end_time, user_id, app_id):
        """
        Updates the end_time of a passage in case it exists

        Parameters
        ----------
        instant : timestamp
            timestamp of the event
        end_time: timestamp
            final timestamp of the event
        user_id : int
            user identifier
        app_id : int
            app identifier
        """
        try:
            if end_time is not None:
                passage = Passage.objects.get(start_time=instant,
                                              person_id=user_id,
                                              app_id=app_id)
                passage.end_time = end_time
                passage.save()
        except DoesNotExist:
            print('Something went wrong, no passage found!')

    def __create_objects(self, summary):
        """
        Creates the objects based on the summary given

        Parameters
        ----------
        summary : xml.etree.ElementTree.Element
            element of the XML file with the information of an event
        """
        event_type = self.__parse_event_type(summary.findtext('Mensaje'))
        instant = self._parse_timestamp(summary.findtext('Hora'))
        start_time = self.__set_start_time(instant, summary.findtext('Duración'))
        item_id = self.__get_item(summary.findtext('IPdeliniciador'))
        user_id = self.__get_user(summary.findtext('Usuario'))
        app_id = self.__get_app('VPN')

        end_time = None
        if start_time is not None:
            end_time = instant
            instant = start_time

        if not super()._check_if_passage_exists(instant=instant, user_id=user_id, app_id=app_id):
            event_id = super()._create_event(instant=instant, end_time=end_time, event_type=event_type)
            super()._create_passage(instant=instant, end_time=end_time,
                                    app_id=app_id, event_id=event_id,
                                    item_id=item_id, user_id=user_id)
        else:
            self.__update_passage(instant, end_time, user_id, app_id)

    def _parse_timestamp(self, timestamp):
        """
        Parses the timestamp given to a format that the ORM can store

        Parameters
        ----------
        timestamp : timestamp
            timestamp of event

        Returns
        -------
        timestamp
            timestamp of event
        """

        units = datetime.datetime.strptime(timestamp, '%d-%b-%Y %H:%M:%S')
        return datetime.datetime.strftime(units, '%Y-%m-%d %H:%M:%S')

    def store_data(self):
        """
        Stores the data into the Event entity and Passage entity
        """
        current = locale.getlocale()
        locale.setlocale(locale.LC_ALL, ('es_US', 'UTF-8'))

        files = self.__file_manager.check_directory()
        roots = self.__file_manager.get_roots(files)
        for root in roots:
            for elements in root.iter():
                for summary in elements.findall('Summary'):
                    self.__create_objects(summary)
        self.__file_manager.move_files(files)

        locale.setlocale(locale.LC_ALL, current)
