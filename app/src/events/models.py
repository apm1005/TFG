from django.db import models
from eventtypes.models import Eventtype


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    instant = models.DateTimeField(blank=True, null=True)
    event_type = models.ForeignKey(Eventtype, models.DO_NOTHING, db_column='event_type', blank=True, null=True)

    def __str__(self):
        return str(self.instant) + ' - ' + str(self.event_type)  # TODO - Fix datetime format, instant shows 00:00?
