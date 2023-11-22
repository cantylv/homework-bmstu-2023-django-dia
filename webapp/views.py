from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    return render(req, 'public/pages/orders_mainPage.html')


def executors(req):
    return render(req, 'public/pages/executors_mainPage.html')


def contractors(req):
    return render(req, 'public/executors.html')


def orders(req):
    return render(req, 'public/orders.html')
