from django.db import models
from itemtypes.models import Itemtype


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_type = models.ForeignKey(Itemtype, models.DO_NOTHING, db_column='item_type', blank=True, null=True)
    ip_address = models.CharField(max_length=17, blank=True, null=True)
    mac_address = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.item_type)
