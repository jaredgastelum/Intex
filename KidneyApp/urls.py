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
from .views import APITotalPageView
from .views import FoodEntryPageView
from .views import FoodEntrySubmitPageView

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
    path("foodentry", FoodEntryPageView, name='FoodEntry'),
    path("foodSubmit/", FoodEntrySubmitPageView, name='FoodEntrySubmit'),
    path("API", APIPageView, name="API"),
    path("APISearch/", APISearchPageView, name='APISearch'),
    path("APISelect/", APISelectPageView, name='APISelect'),
    path("APITotal/", APITotalPageView, name='APITotal'),
    path("popup/", popupPageView, name="popup")
]
