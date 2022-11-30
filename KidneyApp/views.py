from django.shortcuts import render
from django.http import HttpRequest
import urllib.parse
import requests
from .models import Person
from .models import LabVitals
from .models import Morbidity

# Create your views here.


def indexPageView(request):
    return render(request, 'kidneyApp/index.html')


def aboutPageView(request):
    return render(request, 'kidneyApp/about.html')


def dashboardPageView(request):
    data = LabVitals.objects.filter(personID=1)

    K_number = 0
    Phos_number = 0
    Na_number = 0
    Creatinine_number = 0
    Albumin_number = 0
    BloodSugar_number = 0

    iCount = 0

    for datas in data:
        K_number += int(datas.K)
        Phos_number += int(datas.Phos)
        Na_number += int(datas.Na)
        Creatinine_number += int(datas.Creatinine)
        Albumin_number += int(datas.Albumin)
        BloodSugar_number += int(datas.BloodSugar)
        
        iCount += 1

    K_total = K_number / iCount
    Phos_total = Phos_number / iCount
    Na_total = Na_number / iCount
    Creatinine_total = Creatinine_number / iCount
    Albumin_total = Albumin_number / iCount
    BloodSugar_total = BloodSugar_number / iCount

    context = {
        'data': data,
        'K_number' : K_total,
        'Phos_number' : Phos_total,
        'Na_number' : Na_total,
        'Creatinine_number' : Creatinine_total,
        'Albumin_number' : Albumin_total,
        'BloodSugar_number' : BloodSugar_total,
    }

    return render(request, 'kidneyApp/dashboard.html', context)


def profilePageView(request):
    return render(request, 'kidneyApp/profile.html')

def labVitalsPageView(request):
    return render(request, 'kidneyApp/labvitals.html')

def popupPageView(request):
    return render(request, 'kidneyApp/popupForm.html')

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
        new_person.age = request.POST.get(('age'))
        new_person.weight = request.POST.get(('weight'))
        new_person.height = request.POST.get(('height'))

        new_person.save()
        if (request.POST.get('HBP')):
            new_Morbidity = Morbidity.objects.create(name='High Blood Pressure', datediagnosed=request.POST.get('bloodDate'))
            new_person.morbidities.add(new_Morbidity)

        if (request.POST.get('DIA')):
            new_Morbidity = Morbidity.objects.create(name='Diabetes', datediagnosed=request.POST.get('diabetesDate'))
            new_person.morbidities.add(new_Morbidity)

    return render(request, 'kidneyApp/made.html')

def storeVitalsPageView(request):
    if request.method == 'POST':
        person = Person.objects.get(personid=1)

        new_vitals = LabVitals()

        new_vitals.personID = person
        new_vitals.K = request.POST.get('k')
        new_vitals.Phos = request.POST.get('phos')
        new_vitals.Na = request.POST.get('na')
        new_vitals.Creatinine = request.POST.get('creatinine')
        new_vitals.Albumin = request.POST.get('albumin')
        new_vitals.BloodPressure = request.POST.get('blood')
        new_vitals.BloodSugar = request.POST.get('sugar')
        new_vitals.Date = request.POST.get('date')
        new_vitals.Weight = request.POST.get(('weight'))

        new_vitals.save()

    return render(request, 'kidneyApp/dashboard.html', print("Lab Vitals are now Updated"))
       



main_api = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=7x7Fdbbm5dM21Ew53VRae6ienaRTfCSgQxGnpdKM&'

food = 'apple'

url = main_api + urllib.parse.urlencode({'query': food})

json_data = requests.get(url).json()

#print(json_data['foods'][0]['fdcId'])

#new
def APIPageView(request) :
    return render(request, 'kidneyApp/APISearch.html')

def APISearchPageView(request) :
    # Variables from the Search
    sName = request.GET['name']
    iAmount = request.GET['amount']

    # Getting the ID of the specific food
    main_api = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=hzFpuwTYK1oM4XS0SnGp0xJyNVQG7EI4Yq0ZK5dl&dataType=Survey%20%28FNDDS%29&'

    food = sName

    url = main_api + urllib.parse.urlencode({'query': food})

    new = requests.get(url).json()

    newID = new['foods'][0]['fdcId']

    data = {'name': sName.upper(), 'amount': iAmount, 'list': []}

    for iCount in range(0,9):

        data['list'].append({'description': new['foods'][iCount]['description'], 'additional': new['foods'][iCount]['additionalDescriptions'], 'number': new['foods'][iCount]['fdcId']})

    
    # Sending collected data to html
    context = {
        'food' : data
    }

    # Returning a Specific HTML
    return render(request, 'kidneyApp/APIselect.html', context)

def APISelectPageView(request) :
    # Variables from the Search
    sName = request.GET['name']
    iAmount = request.GET['amount']
    newID = request.GET['number']

    # Get Nutrients from ID
    api2 = 'https://api.nal.usda.gov/fdc/v1/food/' + str(newID) + '?api_key=hzFpuwTYK1oM4XS0SnGp0xJyNVQG7EI4Yq0ZK5dl'

    new2 = requests.get(api2).json()

    data = {'name': sName.upper(), 'amount': iAmount, 'all':[]}

    # The Nutrients we need adding them to the list in the data dictionary
    # Water
    data['all'].append({'name': new2['foodNutrients'][1]['nutrient']['name'], 'amount': (str(new2['foodNutrients'][1]['amount'] * float(iAmount)) + ' ' + str(new2['foodNutrients'][1]['nutrient']['unitName']))})

    # Cholesterol
    data['all'].append({'name': new2['foodNutrients'][66]['nutrient']['name'], 'amount': (str(new2['foodNutrients'][66]['amount']  * float(iAmount)) + ' ' + str(new2['foodNutrients'][66]['nutrient']['unitName']))})

    # Sodium, Na
    data['all'].append({'name': new2['foodNutrients'][15]['nutrient']['name'], 'amount': (str(new2['foodNutrients'][15]['amount']  * float(iAmount)) + ' ' + str(new2['foodNutrients'][15]['nutrient']['unitName']))})

    # Phosphorus
    data['all'].append({'name': new2['foodNutrients'][13]['nutrient']['name'], 'amount': (str(new2['foodNutrients'][13]['amount']  * float(iAmount)) + ' ' + str(new2['foodNutrients'][13]['nutrient']['unitName']))})

    # Sugars, total including NLEA
    data['all'].append({'name': new2['foodNutrients'][8]['nutrient']['name'], 'amount': (str(new2['foodNutrients'][8]['amount']  * float(iAmount)) + ' ' + str(new2['foodNutrients'][8]['nutrient']['unitName']))})

    # Potassium, K
    data['all'].append({'name': new2['foodNutrients'][14]['nutrient']['name'], 'amount': (str(new2['foodNutrients'][14]['amount']  * float(iAmount)) + ' ' + str(new2['foodNutrients'][14]['nutrient']['unitName']))})

    # Protein
    data['all'].append({'name': new2['foodNutrients'][3]['nutrient']['name'], 'amount': (str(new2['foodNutrients'][3]['amount']  * float(iAmount)) + ' ' + str(new2['foodNutrients'][3]['nutrient']['unitName']))})

    # Sending collected data to html
    context = {
        'food' : data
    }

    # Returning a Specific HTML
    return render(request, 'kidneyApp/APIdisplay.html', context)