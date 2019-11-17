# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Passage(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey('Event', models.DO_NOTHING, blank=True, null=True)
    app = models.ForeignKey('App', models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey('Item', models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Passage'
