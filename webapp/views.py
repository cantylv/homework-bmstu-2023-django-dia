from django.shortcuts import render
from webapp.database import SERVICES


def home(req):
    services = SERVICES
    filter_criteria = req.GET.get('filter', None)
    if filter_criteria == 'профессия':
        services = sorted(services, key=lambda x: x['job'].lower())

    return render(req, 'public/pages/index.html', {
        'services': services,
        'filter_criteria': filter_criteria
    })


def service(req, service_id):
    selected_service = next((item for item in SERVICES if item['id'] == service_id))
    return render(req, 'public/pages/service.html', {
        'service': selected_service
    })

