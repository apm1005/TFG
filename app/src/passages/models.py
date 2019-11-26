from django.db import models
from applications.models import App
from events.models import Event
from persons.models import Person
from items.models import Item


class Passage(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    app = models.ForeignKey(App, models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.person) + ' - ' + str(self.item) + ' - ' + str(self.app) + ' - ' + str(self.start_time)\
               + ' - ' + str(self.end_time)
