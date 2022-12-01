from django.shortcuts import render, redirect
from django.http import HttpRequest
import urllib.parse
import requests
from .models import Person
from .models import LabVitals
from .models import JournalEntry



# NEW LOGIN IMPORTS
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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

def popupPageView(request):
    return render(request, 'kidneyApp/popupForm.html')

def loginPageView(request):
    return render(request, 'kidneyApp/login.html')

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

       

    
        username = request.POST['username']
        fname = request.POST['fName']
        lname = request.POST['lName']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.objects.filter(username=username):
        #     messages.error(request, "Username already exist! Please enter another username")
        #     return redirect('profile')
        
        # if User.objects.filter(email=email):
        #     messages.error(request, "Email already registered!")
        #     return redirect('profile')

        # if len(username)>10:
        #     messages.error(request, "Username must be under 10 characters")
        
        # if pass1 != pass2 :
        #     messages.error(request, "Passwords didn't match!")

        # if not username.isalnum():
        #     messages.error(request, "Username must include at least 1 letter")
        #     return redirect('profile')


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

    return render(request, 'kidneyApp/index.html', {'fName':fname}, {'lName':lname})

def storeVitalsPageView(request):
    if request.method == 'POST':

        new_vitals = LabVitals()

        new_vitals.personID = request.POST.get('personid')
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


def journalPageView(request):
    if request.method == 'POST':
        new_journal = JournalEntry()

        new_journal.notes = request.POST.get('journalentry')
        new_journal.date = request.POST.get('date')
        new_journal.status = request.POST.get('status')


        new_journal.save()

    return render(request, 'kidneyApp/dashboard.html', print("Journal Entry Created"))

       



main_api = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=7x7Fdbbm5dM21Ew53VRae6ienaRTfCSgQxGnpdKM&'

food = 'apple'

url = main_api + urllib.parse.urlencode({'query': food})

json_data = requests.get(url).json()

print(json_data['foods'][0]['fdcId'])

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



#NEW LOGIN SCREEN
def newLoginPageView(request):
    return render(request, 'kidneyApp/newLogin.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')


    return render(request, "kidneyApp/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "kidneyApp/index.html", {'fName':fname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('newLogin')

    return render(request, "kidneyApp/login.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('index')