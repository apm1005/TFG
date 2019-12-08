import xml.etree.ElementTree as et
import datetime
from os import listdir, chdir
from persons.models import Person
from eventtypes.models import Eventtype
from events.models import Event
from applications.models import App
from passages.models import Passage
from items.models import Item


class VPNParser:
    """
    Class that reads logs of the VPN and stores it in the database.
    """

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
    def __check_directory():
        """
        Checks if there are VPN XML files to parse and returns a list with the names

        Returns
        -------
        list
            a list with all the names of the XML files
        """
        return listdir('..\\log_examples\\vpn_logs')

    @staticmethod
    def __create_event(instant, event_type):
        """
        Creates an event for an instant and type of event specified

        Parameters
        ----------
        instant : timestamp
            timestamp of the event
        event_type : str
            type of the event

        Returns
        -------
        int
            an int that identifies an event
        """
        identifier = None
        try:
            type_of_event = Eventtype.objects.get(type=event_type)
            event = Event.objects.create(instant=instant, event_type=type_of_event)
            event.save()
            identifier = event.id
        except DoesNotExist:
            print(f'Type of event not found {event_type}!')
        finally:
            return identifier

    @staticmethod
    def __parse_timestamp(timestamp):
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
    def __create_passage(instant, end_time, app_id, event_id, item_id, user_id):
        """
        Creates a Passage in the database
        """
        Passage.objects.create(start_time=instant,
                               end_time=end_time,
                               app_id=app_id,
                               event_id=event_id,
                               item_id=item_id,
                               person_id=user_id)

    def __create_objects(self, summary):
        """
        Creates the objects based on the summary given

        Parameters
        ----------
        summary : xml.etree.ElementTree.Element
            element of the XML file with the information of an event
        """
        event_type = self.__parse_event_type(summary.findtext('Mensaje'))
        instant = self.__parse_timestamp(summary.findtext('Hora'))
        start_time = self.__set_start_time(instant, summary.findtext('Duración'))
        item_id = self.__get_item(summary.findtext('IPdeliniciador'))
        user_id = self.__get_user(summary.findtext('Usuario'))
        app_id = self.__get_app('VPN')

        end_time = None
        if start_time is not None:
            end_time = instant
            instant = start_time
            event_type = 'log in'

        event_id = self.__create_event(instant=instant, event_type=event_type)
        self.__create_passage(instant=instant,
                              end_time=end_time,
                              app_id=app_id,
                              event_id=event_id,
                              item_id=item_id,
                              user_id=user_id)

    def __store_data(self):
        """
        Stores the data into the Event entity and Passage entity
        """
        files = self.__check_directory()
        roots = [et.parse(f'../log_examples/vpn_logs/{file}').getroot() for file in files]
        for root in roots:
            for elements in root.iter():
                for summary in elements.findall('Summary'):
                    self.__create_objects(summary)

    def parse(self):
        """
        Parses the events of the VPN and stores them in the database.
        """
        self.__store_data()
