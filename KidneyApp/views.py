from django.shortcuts import render
from django.http import HttpRequest
import urllib.parse
import requests
from .models import Person
from .models import Patient

# Create your views here.


def indexPageView(request):
    return render(request, 'kidneyApp/index.html')


def aboutPageView(request):
    return render(request, 'kidneyApp/about.html')


def dashboardPageView(request):
    return render(request, 'kidneyApp/dashboard.html')


def profilePageView(request):
    return render(request, 'kidneyApp/profile.html')

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

        new_patient = Patient()

        new_patient.age = request.POST.get('age')
        new_patient.weight = request.POST.get('weight')
        new_patient.height = request.POST.get('height')

        new_patient.save()

    return render('kidneyApp/made.html')


        



main_api = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=7x7Fdbbm5dM21Ew53VRae6ienaRTfCSgQxGnpdKM&'

food = 'apple'

url = main_api + urllib.parse.urlencode({'query': food})

json_data = requests.get(url).json()

print(json_data['foods'][0]['fdcId'])