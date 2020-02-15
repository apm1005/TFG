from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    TemplateView,
)
from .models import Passage, Person


class HomeView(TemplateView):
    template_name = 'logscope/home.html'


class PassageListView(ListView):
    model = Passage
    template_name = 'logscope/passage.html'
    context_object_name = 'passages'
    paginate_by = 10

    def get_queryset(self):
        """Method to filter a search by person, app and date"""
        filter_set = Passage.objects.all()

        if self.request.GET.get('person'):
            person = self.request.GET.get('person')
            filter_set = filter_set.filter(person__login__icontains=person)

        if self.request.GET.get('date'):
            date = self.request.GET.get('date')
            filter_set = filter_set.filter(start_time__icontains=date)

        if self.request.GET.get('app'):
            app = self.request.GET.get('app')
            filter_set = filter_set.filter(app__name__icontains=app)

        if self.request.GET.get('item'):
            item = self.request.GET.get('item')
            filter_set = filter_set.filter(item__item_type__type__icontains=item)

        return filter_set.order_by('-start_time')


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
