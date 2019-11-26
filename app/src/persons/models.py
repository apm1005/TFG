from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.login) + ' - ' + str(self.name)
