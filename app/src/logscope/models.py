from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=False)
    login = models.CharField(max_length=20, blank=True, null=False)
    company = models.CharField(max_length=50, blank=True, null=False)
    division = models.CharField(max_length=50, blank=True, null=False)
    area = models.CharField(max_length=50, blank=True, null=False)
    department = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):
        return str(self.login)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['login'], name='unique user login')
        ]


class Itemtype(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30, null=False)
    brand = models.CharField(max_length=30, blank=True, null=False)
    model = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):
        return str(self.type) + ' | ' + str(self.brand) + ' ' + str(self.model)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_type = models.ForeignKey(Itemtype, models.DO_NOTHING, db_column='item_type', blank=True, null=True)
    ip_address = models.CharField(max_length=17, blank=True, null=True)
    mac_address = models.CharField(max_length=20, blank=True, null=True)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return str(self.item_type)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['mac_address'], name='unique mac address')
        ]


class Eventtype(models.Model):
    type = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.type


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    instant = models.DateTimeField(blank=True, null=False)
    event_type = models.ForeignKey(Eventtype, models.DO_NOTHING, db_column='event_type', blank=True, null=False)

    def __str__(self):
        return str(self.instant) + ' - ' + str(self.event_type)


class Environment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=False)
    ip_address = models.CharField(max_length=17, blank=True, null=True)

    def __str__(self):
        return self.server


class App(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    server = models.ForeignKey(Environment, models.DO_NOTHING, db_column='server', blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Passage(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, null=False)
    app = models.ForeignKey(App, models.DO_NOTHING, null=False)
    person = models.ForeignKey(Person, models.DO_NOTHING, null=False)
    item = models.ForeignKey(Item, models.DO_NOTHING, null=True)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.person) + ' - ' + str(self.item) + ' - ' + str(self.app) + ' - ' + str(self.start_time)\
               + ' - ' + str(self.end_time)

    @property
    def duration(self):
        return self.end_time - self.start_time if self.end_time is not None else 'Unknown'
