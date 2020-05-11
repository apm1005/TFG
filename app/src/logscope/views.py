from django.utils.decorators import method_decorator
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
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom


class HomeView(TemplateView):
    template_name = 'logscope/home.html'


@method_decorator(login_required, name='dispatch')
class PassageTableView(ExportMixin, SingleTableMixin, FilterView):
    model = Passage
    template_name = 'logscope/passage.html'
    table_class = PassageTable
    filterset_class = PassageFilter


@method_decorator(login_required, name='dispatch')
class StatisticView(TemplateView):
    template_name = 'logscope/statistic.html'


@method_decorator(login_required, name='dispatch')
class AnalyticsView(TemplateView):
    template_name = 'logscope/analytics.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! Log in!')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'logscope/register.html', {'form': form})
