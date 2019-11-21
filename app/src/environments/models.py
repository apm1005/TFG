from django.db import models


class Environment(models.Model):
    server = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=17, blank=True, null=True)
