from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import dashboardPageView
from .views import profilePageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about', aboutPageView, name='about'),
    path('dashboard', dashboardPageView, name='dashboard'),
    path('profile', profilePageView, name='profile'),
]
