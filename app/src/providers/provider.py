from abc import ABC, abstractmethod
from logscope.models import (
    App,
    Eventtype,
    Event,
    Item,
    Passage,
    Person,
)


class Provider(ABC):
    """
    Class that analyzes content from the logs of each app and provides data for the database.
    """

    def provide(self):
        """
        Template method
        """
        self.store_data()

    @staticmethod
    def _create_event(instant, end_time, event_type):
        """
        Creates an event for an instant and type of event specified

        Parameters
        ----------
        instant : timestamp
            timestamp of the event
        end_time : timestamp
            final timestamp of the event
        event_type : str
            type of the event

        Returns
        -------
        int
            an int that identifies an event
        """
        identifier = None
        if end_time is not None:
            instant = end_time
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
    def _create_passage(instant, end_time, app_id, event_id, item_id, user_id):
        """
        Creates a Passage in the database

        Parameters
        ----------
        instant : timestamp
            timestamp of the event
        end_time : timestamp
            final timestamp of the event
        app_id : int
            app identifier
        event_id : int
            event identifier
        item_id : int
            item identifier
        user_id : int
            user identifier
        """
        Passage.objects.create(start_time=instant,
                               end_time=end_time,
                               app_id=app_id,
                               event_id=event_id,
                               item_id=item_id,
                               person_id=user_id)

    @staticmethod
    def _check_if_passage_exists(instant, user_id, app_id):
        """
        Checks if a passage is already in the database

        Parameters
        ----------
        instant : timestamp
            timestamp of the event
        user_id : int
            user identifier
        app_id : int
            app identifier

        Returns
        -------
        boolean
            True if the passage is already in the database
            False if the passage is not in the database
        """
        exists = None
        try:
            Passage.objects.get(start_time=instant,
                                person_id=user_id,
                                app_id=app_id)
            exists = True
        except DoesNotExist:
            exists = False
        finally:
            return exists

    @abstractmethod
    def _parse_timestamp(self, timestamp):
        """
        Parses the timestamp given to a format that the ORM can store

        Parameters
        ----------
        timestamp : timestamp
            event timestamp
        """
        pass

    @abstractmethod
    def store_data(self):
        """
        Stores the data into the Event and Passage entities
        """
        pass
