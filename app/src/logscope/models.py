from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.login) + ' - ' + str(self.name)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['login'], name='unique user login')
        ]


class Itemtype(models.Model):
    type = models.CharField(primary_key=True, max_length=30)
    model = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.type) + ' | ' + str(self.model)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_type = models.ForeignKey(Itemtype, models.DO_NOTHING, db_column='item_type', blank=True, null=True)
    ip_address = models.CharField(max_length=17, blank=True, null=True)
    mac_address = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.item_type)


class Personitems(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)

    def __str__(self):
        return str(self.person) + ' - ' + str(self.item)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['person', 'item'], name='unique person item')
        ]


class Eventtype(models.Model):
    type = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.type


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    instant = models.DateTimeField(blank=True, null=True)
    event_type = models.ForeignKey(Eventtype, models.DO_NOTHING, db_column='event_type', blank=True, null=True)

    def __str__(self):
        return str(self.instant) + ' - ' + str(self.event_type)


class Environment(models.Model):
    server = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=17, blank=True, null=True)

    def __str__(self):
        return self.server


class App(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    server = models.ForeignKey(Environment, models.DO_NOTHING, db_column='server', blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.server)


class Passage(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    app = models.ForeignKey(App, models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.person) + ' - ' + str(self.item) + ' - ' + str(self.app) + ' - ' + str(self.start_time)\
               + ' - ' + str(self.end_time)
