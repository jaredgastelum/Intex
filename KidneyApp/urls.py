from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import dashboardPageView
from .views import profilePageView
from .views import storeProfilePageView
from .views import storeVitalsPageView
from .views import labVitalsPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about', aboutPageView, name='about'),
    path('dashboard', dashboardPageView, name='dashboard'),
    path('profile', profilePageView, name='profile'),
    path('labvitals', labVitalsPageView, name="labvitals"),
    path("storeprofile", storeProfilePageView, name="storeProfile"),
    path('storevitals', storeVitalsPageView, name='storevitals'),
]
