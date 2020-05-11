from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView,
    PassageTableView,
    StatisticView,
    AnalyticsView,
    register,
)

urlpatterns = [
    path('', HomeView.as_view(), name='logscope-home'),
    path('passage/', PassageTableView.as_view(), name='passage'),
    path('statistic/', StatisticView.as_view(), name='statistic'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='logscope/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logscope/logout.html'), name='logout'),
]
