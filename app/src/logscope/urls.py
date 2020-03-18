from django.urls import path
from .views import (
    HomeView,
    PassageTableView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='logscope-home'),
    path('passage/', PassageTableView.as_view(), name='passage'),
]
