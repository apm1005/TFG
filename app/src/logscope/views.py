from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
)
from .models import Passage


def home(request):
    return render(request, 'logscope/home.html')


class PassageListView(ListView):
    model = Passage
    template_name = 'logscope/passage.html'
    context_object_name = 'passages'
    ordering = ['-start_time']


class PassageDetailView(DetailView):
    model = Passage


class PassageDeleteView(DeleteView):
    model = Passage
    success_url = '/passage'
