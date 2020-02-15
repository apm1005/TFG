from django.shortcuts import get_object_or_404
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
    ordering = ['-start_time']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('person') is not None:
            person = self.request.GET.get('person')
            qs = qs.filter(person__login__icontains=person)

        if self.request.GET.get('date') is not None:
            date = self.request.GET.get('date')
            qs = qs.filter(start_time__icontains=date)

        if self.request.GET.get('app') is not None:
            app = self.request.GET.get('app')
            qs = qs.filter(app__name__icontains=app)

        if self.request.GET.get('item') is not None:
            item = self.request.GET.get('item')
            qs = qs.filter(item__item_type__type__icontains=item)

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
