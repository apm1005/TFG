from django_tables2 import Table

from .models import Passage


class PassageTable(Table):
    class Meta:
        model = Passage
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', 'person__name', 'person__area', 'app__name', 'start_time', 'duration', 'item__item_type')
