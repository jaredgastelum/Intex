from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import dashboardPageView
from .views import profilePageView
from .views import storeProfilePageView
from .views import storeVitalsPageView
from .views import labVitalsPageView

#new 
from .views import APIPageView
from .views import APISearchPageView
from .views import APISelectPageView

#test
from .views import popupPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about', aboutPageView, name='about'),
    path('dashboard', dashboardPageView, name='dashboard'),
    path('profile', profilePageView, name='profile'),
    path('labvitals', labVitalsPageView, name="labvitals"),
    path("storeprofile", storeProfilePageView, name="storeProfile"),
    path('storevitals', storeVitalsPageView, name='storevitals'),
    path("API", APIPageView, name="API"),
    path("APISearch/", APISearchPageView, name='APISearch'),
    path("APISelect/", APISelectPageView, name='APISelect'),
    path("popup/", popupPageView, name="popup")
]
