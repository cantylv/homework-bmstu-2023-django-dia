# Локальная база данных

import random

# Каталоги заказов/исполнителей

CATALOGS = [
    {
        'id': 1,
        "name": "Доставка и логистика",
        "url_name": "delivery",
        "src": "svg/orders/delivery.svg"
    },
    {
        'id': 2,
        "name": "Торговля",
        "url_name": "trading",
        "src": "svg/orders/trading.svg"
    },
    {
        "id": 3,
        "name": "Услуги и прочее",
        "url_name": "other",
        "src": "svg/orders/other.svg"
    },
    {
        "id": 4,
        "name": "Менеджмент, продажи, администрирование",
        "url_name": "management",
        "src": "svg/orders/management.svg"
    },
    {
        "id": 5,
        "name": "Строительство, ремонт, производство",
        "url_name": "construction",
        "src": "svg/orders/construction.svg"
    },

    {
        "id": 6,
        "name": "СМИ",
        "url_name": "media",
        "src": "svg/orders/media.svg"
    },

    {
        "id": 7,
        "name": "Разработка ПО",
        "url_name": "it",
        "src": "svg/orders/it.svg"
    },

    {
        "id": 8,
        "name": "Проектирование",
        "url_name": "engineering",
        "src": "svg/orders/engineering.svg"
    },

    {
        "id": 9,
        "name": "Дизайн",
        "url_name": "design",
        "src": "svg/orders/design.svg"
    },

    {
        "id": 10,
        "name": "Финансы и бухгалтерия",
        "url_name": "finance",
        "src": "svg/orders/finance.svg"
    },

    {
        "id": 11,
        "name": "HoReCa",
        "url_name": "horeca",
        "src": "svg/orders/horeca.svg"
    },
    {
        "id": 12,
        "name": "Маркетинг",
        "url_name": "marketing",
        "src": "svg/orders/marketing.svg"
    },
    {
        "id": 13,
        "name": "Красота и здоровье",
        "url_name": "beauty",
        "src": "/svg/orders/beauty.svg"
    },
]


CATALOGS_NAME_ID = {
    'delivery': 1,
    'trading': 2,
    'other': 3,
    'management': 4,
    'construction': 5,
    'media': 6,
    'it': 7,
    'engineering': 8,
    'design': 9,
    'finance': 10,
    'horeca': 11,
    'marketing': 11,
    'beauty': 11,

}


ORDERS = [
    {
        'id': i,
        'catalog_id': random.randint(1, 13),
        'title': f'Работа такая-то № {i}',
        'owner': f'Company{i}',
        'ownerPicture': 'img/user1.jpg',
        'ownerShortInfo': f'blablalba{i}',
        'ownerPlace': f'office{i}',
        'period': f'ii.ii.iii{i}',
        'job': f'job {i}',
        'place': f'place{i}',
        'salary': f'{i * i}',
        'contract': f'contract{i}',
        'condition': f'no',
        'aboutDeal': f'you need to do it{i}'
    } for i in range(500)
]

CONTRACTORS = [
    {
        'id': i,
        'catalog_id': random.randint(1, 13),
        'name': f'Name{i}',
        'picture': 'img/user1.jpg',
        'job': f'job {i}',
        'another_skills': f'job-job{i}',
        'age': f'1{i}',
        'sex': 'male',
        'citship': f'citizenship{i}',
        'townJob': f'Town{i}',
        'languages': 'English',
        'another_townJob': f'Town Another {i}',
        'salary': f'{i * i}',
        'medBook': 'Yes',
        'contraindications': 'None',
        'schedule': '1/3',
    } for i in range(50)
]
