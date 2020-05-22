from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView,
    PassageTableView,
    AnalyticsView,
    MicrosoftAnalyticsView,
    LocationAnalyticsView,
    WikiView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='logscope-home'),
    path('passage/', PassageTableView.as_view(), name='passage'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('microsoft_analytics/', MicrosoftAnalyticsView.as_view(), name='microsoft_analytics'),
    path('usage_by_location/', LocationAnalyticsView.as_view(), name='usage_by_location'),
    path('login/', auth_views.LoginView.as_view(template_name='logscope/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logscope/logout.html'), name='logout'),
    path('wiki/', WikiView.as_view(), name='wiki'),
]
