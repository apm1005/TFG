from django.views.generic import (
    TemplateView,
)
from django.contrib.auth.decorators import login_required
from .models import Passage
from .tables import PassageTable
from .filters import PassageFilter
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django_filters.views import FilterView


class HomeView(TemplateView):
    template_name = 'logscope/home.html'


class PassageTableView(ExportMixin, SingleTableMixin, FilterView):
    model = Passage
    template_name = 'logscope/passage.html'
    table_class = PassageTable
    filterset_class = PassageFilter


class StatisticView(TemplateView):
    template_name = 'logscope/statistic.html'


class AnalyticsView(TemplateView):
    template_name = 'logscope/analytics.html'
