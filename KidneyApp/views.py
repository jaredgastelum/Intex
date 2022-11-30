from django.shortcuts import render
from django.http import HttpRequest
import urllib.parse
import requests
from .models import Person
from .models import Patient
from .models import LabVitals

# Create your views here.


def indexPageView(request):
    return render(request, 'kidneyApp/index.html')


def aboutPageView(request):
    return render(request, 'kidneyApp/about.html')


def dashboardPageView(request):
    return render(request, 'kidneyApp/dashboard.html')


def profilePageView(request):
    return render(request, 'kidneyApp/profile.html')

def labVitalsPageView(request):
    return render(request, 'kidneyApp/labvitals.html')

def storeProfilePageView(request):
    if request.method == 'POST':
        new_person = Person()

        new_person.first_name = request.POST.get('fName')
        new_person.last_name = request.POST.get('lName')
        new_person.phone = request.POST.get('phone')
        new_person.email = request.POST.get('email')
        new_person.address = request.POST.get('address')
        new_person.city = request.POST.get('city')
        new_person.state = request.POST.get('state')
        new_person.zip = request.POST.get('zipcode')

        new_person.save()

        '''
        new_patient = Patient()

        new_patient.age = request.POST.get(int('age'))
        new_patient.weight = request.POST.get(int('weight'))
        new_patient.height = request.POST.get(int('height'))

        new_patient.save()
        '''

    return render('kidneyApp/made.html')

def storeVitalsPageView(request):
    if request.method == 'POST':

        new_vitals = LabVitals()

        new_vitals.K = request.POST.get('k')
        new_vitals.Phos = request.POST.get('phos')
        new_vitals.Na = request.POST.get('na')
        new_vitals.creatinine = request.POST.get('creatinine')
        new_vitals.Albumin = request.POST.get('albumin')
        new_vitals.BloodPressure = request.POST.get('blood')
        new_vitals.BloodSugar = request.POST.get('sugar')
        new_vitals.Date = request.POST.get('date')
        new_vitals.Weight = request.POST.get(int('weight'))

        new_vitals.save()

    return render('kidneyApp/dashboard.html', print("Lab Vitals are now Updated"))
       



main_api = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=7x7Fdbbm5dM21Ew53VRae6ienaRTfCSgQxGnpdKM&'

food = 'apple'

url = main_api + urllib.parse.urlencode({'query': food})

json_data = requests.get(url).json()

print(json_data['foods'][0]['fdcId'])