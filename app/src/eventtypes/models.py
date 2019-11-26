from django.db import models


class Eventtype(models.Model):
    type = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.type
