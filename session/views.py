from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return render(request, 'session/index.html')


def entrance(request):
    return render(request, 'session/entrance.html')


def login(request):
    return render(request, 'session/login.html')

