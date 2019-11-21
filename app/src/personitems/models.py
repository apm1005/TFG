from django.db import models
from items.models import Item
from persons.models import Person


class Personitems(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)

    class Meta:
        unique_together = (('person', 'item'),)
