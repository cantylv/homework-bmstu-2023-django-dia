from django.shortcuts import render
from webapp.database import SERVICES


def home(req):
    return render(req, 'public/pages/index.html', {
        'services': SERVICES
    })


def service(req, service_id):
    selected_service = next((item for item in SERVICES if item['id'] == service_id))
    return render(req, 'public/pages/service.html', {
        'service': selected_service
    })

