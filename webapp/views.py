from django.shortcuts import render
from django.core.paginator import Paginator
from webapp.database import CATALOGS, ORDERS, CONTRACTORS, CATALOGS_NAME_ID


def filter_objects_by_substring(objects, search_string, field):
    return [obj for obj in objects if search_string.lower() in obj[field].lower()]


def paginate(req, db_name, db, per_page=5):
    catalog_name = req.GET.get('catalog')  # так лучше не делать, но я это пишу чтобы работал поиск
    catalog_id = CATALOGS_NAME_ID.get(catalog_name)    # на главной странице
    page = int(req.GET.get('page'))
    sort = req.GET.get('sorted')

    if sort:
        if sort == "name":
            if db_name == "ORDERS":
                db = sorted(db, key=lambda item: item['job'])
            elif db_name == "CONTRACTORS":
                db = sorted(db, key=lambda item: item['name'])
        elif sort == "price_asc":
            db = sorted(db, key=lambda item: item['salary'])
        elif sort == "price_desc":
            db = sorted(db, key=lambda item: item['salary'], reverse=True)

    items = [item for item in db if item['catalog_id'] == catalog_id]
    p = Paginator(items, per_page)
    return p.page(page)


# Заказы

def home(req):
    return render(req, 'public/pages/orders_mainPage.html', {
        'catalogs': CATALOGS,
        'page': 1,
        'url_alias': 'orders'
    })


def orders(req):
    db = ORDERS

    if req.GET.get('job'):
        substring = req.GET.get('job')
        db = filter_objects_by_substring(db, substring, 'job')

    catalog_orders = paginate(req, 'ORDERS', db)
    return render(req, 'public/pages/orders_listing.html', {
        'orders': catalog_orders,
        'request': req,
        'url_alias': 'orders'
    })


def order(req, order_id):
    selected_order = next((item for item in ORDERS if item['id'] == order_id))
    return render(req, 'public/pages/order.html', {
        'order': selected_order
    })


# Исполнители


def executors(req):
    return render(req, 'public/pages/executors_mainPage.html', {
        'catalogs': CATALOGS,
        'page': 1,
        'url_alias': 'contractors'
    })


def contractors(req):
    db = CONTRACTORS

    if req.GET.get('name'):
        substring = req.GET.get('name')
        db = filter_objects_by_substring(db, substring, 'name')

    catalog_executors = paginate(req, 'CONTRACTORS', db)
    return render(req, 'public/pages/executors_listing.html', {
        'contractors': catalog_executors,
        'request': req,
        'url_alias': 'contractors'
    })


def contractor(req, contractor_id):
    selected_contractor = next((item for item in CONTRACTORS if item['id'] == contractor_id))
    return render(req, 'public/pages/executor.html', {
        'contractor': selected_contractor
    })
