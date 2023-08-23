from django.shortcuts import render
from .views import iphone, samsung, redmi
from django.urls import path

urlpatterns = [
    path('iphone/', iphone),
    path('samsung/', samsung),
    path('redmi/', redmi)
]