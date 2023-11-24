from django.shortcuts import render
from webapp.database import CATALOGS, ORDERS, CONTRACTORS
import random


# Заказы


def home(req):
    return render(req, 'public/pages/orders_mainPage.html', {
        'catalogs': CATALOGS
    })


def orders(req):  # тут нужно дописать логику с get-параметрами, идущими в качестве параметров
    catalog_id = int(req.GET.get('catalog_id', -1))
    items = [item for item in ORDERS if item['catalog_id'] == catalog_id]
    print(items)
    return render(req, 'public/pages/orders_listing.html', {
        'orders': items
    })


def order(req, order_id):  # тут нужно дописать логику с get-параметрами, идущими в качестве параметров
    selected_order = next((item for item in ORDERS if item['id'] == order_id), -1)
    return render(req, 'public/pages/order.html', {
        'order': selected_order
    })


# Исполнители


def executors(req):
    return render(req, 'public/pages/executors_mainPage.html')


def contractors(req):  # тут нужно дописать логику с get-параметрами, идущими в качестве параметров
    return render(req, 'public/pages/executors_listing.html')


def contractor(req):  # тут нужно дописать логику с get-параметрами, идущими в качестве параметров
    return render(req, 'public/pages/executor.html')
