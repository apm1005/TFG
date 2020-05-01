import django_filters
from .models import Passage


# Fields that appear in the template (even in comments) must be included here
class PassageFilter(django_filters.FilterSet):
    person = django_filters.CharFilter(field_name='person__name', label='Person', lookup_expr='icontains')
    company = django_filters.CharFilter(field_name='person__company', label='Company', lookup_expr='icontains')
    area = django_filters.CharFilter(field_name='person__area', label='Area', lookup_expr='icontains')
    department = django_filters.CharFilter(field_name='person__department', label='Department', lookup_expr='icontains')
    start_time_gt = django_filters.DateTimeFilter(field_name='start_time', label='Start time (date greater than)',
                                                  lookup_expr='date__gte',
                                                  input_formats=["%d/%m/%Y", "%d-%m-%Y"])
    start_time_lt = django_filters.DateTimeFilter(field_name='start_time', label='Start time (date lower than)',
                                                  lookup_expr='date__lte',
                                                  input_formats=["%d/%m/%Y", "%d-%m-%Y"])

    class Meta:
        model = Passage
        fields = ('person', 'app',)
