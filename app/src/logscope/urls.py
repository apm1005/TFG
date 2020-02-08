from django.urls import path
from .views import (
    PassageListView,
    PassageDetailView,
    PassageDeleteView,
)
from . import views


urlpatterns = [
    path('', views.home, name='logscope-home'),
    path('passage/', PassageListView.as_view(), name='logscope-passage'),
    path('passage/<int:pk>/', PassageDetailView.as_view(), name='passage-detail'),
    path('passage/<int:pk>/delete/', PassageDeleteView.as_view(), name='passage-delete'),
]
