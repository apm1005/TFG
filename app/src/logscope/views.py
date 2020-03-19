from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    TemplateView,
)
from .models import App, Itemtype, Passage, Person
from datetime import datetime
from tfgproject.settings import PAGINATION
from .tables import PassageTable
from .filters import PassageFilter
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView


class PassageTableView(SingleTableMixin, FilterView):
    model = Passage
    template_name = 'logscope/passage.html'
    table_class = PassageTable
    filterset_class = PassageFilter


class HomeView(TemplateView):
    template_name = 'logscope/home.html'


class PassageTableExport(SingleTableMixin):
    model = Passage
    table_class = PassageTable
    template_name = 'django_tables2/bootstrap4.html'
