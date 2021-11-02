from django.conf.urls import url,include
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

