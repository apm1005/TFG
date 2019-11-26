from django.db import models


class Itemtype(models.Model):
    type = models.CharField(primary_key=True, max_length=30)
    model = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.type) + ' | ' + str(self.model)
