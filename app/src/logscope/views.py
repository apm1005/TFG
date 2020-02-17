from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    TemplateView,
)
from .models import App, Passage, Person
from datetime import datetime


class HomeView(TemplateView):
    template_name = 'logscope/home.html'


class PassageListView(TemplateView):
    template_name = 'logscope/passage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apps'] = App.objects.distinct()
        return context


class PassageSearchView(ListView):
    model = Passage
    template_name = 'logscope/passage_search.html'
    context_object_name = 'passages'
    ordering = ['-start_time']

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.GET.get('person') != '':
            qs = qs.filter(person__login__icontains=self.request.GET.get('person'))

        if self.request.GET.get('date_gt') != '':
            qs = qs.filter(start_time__date__gte=self.request.GET.get('date_gt'))

        if self.request.GET.get('date_lt') != '':
            qs = qs.filter(start_time__date__lte=self.request.GET.get('date_lt'))

        if self.request.GET.get('hour_gt') != '':
            qs = qs.filter(start_time__hour__gte=datetime.strptime(str(self.request.GET.get('hour_gt')), '%H:%M').hour)

        if self.request.GET.get('hour_lt') != '':
            qs = qs.filter(start_time__hour__lte=datetime.strptime(str(self.request.GET.get('hour_lt')), '%H:%M').hour)

        if self.request.GET.get('app') != '':
            qs = qs.filter(app__name__icontains=self.request.GET.get('app'))

        if self.request.GET.get('item') != '':
            qs = qs.filter(item__item_type__type__icontains=self.request.GET.get('item'))

        return qs.order_by('-start_time')


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
