from django.urls import path
from .views import (
    HomeView,
    PassageListView,
    PassageDetailView,
    PassageDeleteView,
    PassageSearchView,
    PersonPassageListView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='logscope-home'),
    path('passage/', PassageListView.as_view(), name='passage'),
    path('passage/search/', PassageSearchView.as_view(), name='passage-search'),
    path('passage/<int:pk>/', PassageDetailView.as_view(), name='passage-detail'),
    path('passage/<int:pk>/delete/', PassageDeleteView.as_view(), name='passage-delete'),
    path('person/<str:name>/', PersonPassageListView.as_view(), name='person-passages'),
]
