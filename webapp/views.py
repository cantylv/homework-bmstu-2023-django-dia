from django.shortcuts import render
from django.http import HttpResponse


# Заказы

def home(req):
    return render(req, 'public/pages/orders_mainPage.html')


def orders(req):
    return render(req, 'public/pages/orders_listing.html')


def order(req):
    return render(req, 'public/order.html')


# Исполнители

def executors(req):
    return render(req, 'public/pages/executors_mainPage.html')


def contractors(req):
    return render(req, 'public/pages/executors_listing.html')


def contractor(req):
    return render(req, 'public/executor.html')



