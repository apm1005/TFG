from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
)
from .models import Passage, Person


def home(request):
    return render(request, 'logscope/home.html')


class PassageListView(ListView):
    model = Passage
    template_name = 'logscope/passage.html'
    context_object_name = 'passages'
    ordering = ['-start_time']
    paginate_by = 10


class PersonPassageListView(ListView):
    model = Passage
    template_name = 'logscope/person_passages.html'
    context_object_name = 'passages'
    paginate_by = 10

    def get_queryset(self):
        person = get_object_or_404(Person, name=self.kwargs.get('name'))
        return Passage.objects.filter(person=person).order_by('-start_time')


class PassageDetailView(DetailView):
    model = Passage


class PassageDeleteView(DeleteView):
    model = Passage
    success_url = '/passage'
