from django.shortcuts import render
from django.http import HttpResponse


def orders(req):
    return render(req, 'public/orders.html')


def executors(req):
    return render(req, 'public/executors.html')
