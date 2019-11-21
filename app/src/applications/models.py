from django.db import models
from environments.models import Environment


class App(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    server = models.ForeignKey(Environment, models.DO_NOTHING, db_column='server', blank=True, null=True)
