import django_filters
from .models import Passage


class PassageFilter(django_filters.FilterSet):
    start_time__date__gt = django_filters.DateFilter(label='Start time date greater than', lookup_expr='date__gt')
    start_time__date__lt = django_filters.DateFilter(label='Start time date lower than', lookup_expr='date__lt')
    start_time__hour__gt = django_filters.TimeFilter(label='Start time hour greater than', lookup_expr='hour__gt')
    start_time__hour__lt = django_filters.TimeFilter(label='Start time hour lower than', lookup_expr='hour__lt')

    class Meta:
        model = Passage
        fields = ('person', 'app', 'item')
