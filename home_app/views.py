from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Home Application')


def homeApp(request):
    return HttpResponse('my_site/home')