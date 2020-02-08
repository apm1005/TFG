from django.contrib import admin
from .models import (
    App,
    Environment,
    Event,
    Eventtype,
    Item,
    Itemtype,
    Passage,
    Personitems,
    Person,
)


admin.site.register(App)
admin.site.register(Environment)
admin.site.register(Event)
admin.site.register(Eventtype)
admin.site.register(Item)
admin.site.register(Itemtype)
admin.site.register(Passage)
admin.site.register(Personitems)
admin.site.register(Person)

