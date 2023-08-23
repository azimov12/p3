from django.urls import path
from django.http import HttpResponse
# Create your views here.

def iphone(request):
    return HttpResponse('This is iphone')

def samsung(request):
    return HttpResponse('This is samsung')    

def redmi(request):
    return HttpResponse('This is redmi')