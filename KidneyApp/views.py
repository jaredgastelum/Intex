from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def indexPageView(request):
    return render(request, 'kidneyApp/index.html')


def aboutPageView(request):
    return render(request, 'kidneyApp/about.html')


def dashboardPageView(request):
    return render(request, 'kidneyApp/dashboard.html')


def profilePageView(request):
    return render(request, 'kidneyApp/profile.html')
