from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
)
from .models import Passage


class PassageListView(ListView):
    model = Passage
    template_name = 'logscope/home.html'
    context_object_name = 'passages'
    ordering = ['-start_time']


class PassageDetailView(DetailView):
    model = Passage


class PassageDeleteView(DeleteView):
    model = Passage
    success_url = '/passage'
