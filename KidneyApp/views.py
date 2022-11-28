from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def indexPageView(request):
    return render(request, 'kidneyApp/index.html')
