# Локальная база данных

import random

# Каталоги заказов/исполнителей

CATALOGS = [
    {
        'id': 1,
        "name": "Доставка и логистика",
        "src": "svg/orders/delivery.svg"
    },
    {
        'id': 2,
        "name": "Торговля",
        "src": "svg/orders/trading.svg"
    },
    {
        "id": 3,
        "name": "Услуги и прочее",
        "src": "svg/orders/other.svg"
    },
    {
        "id": 4,
        "name": "Менеджмент, продажи, администрирование",
        "src": "svg/orders/management.svg"
    },
    {
        "id": 5,
        "name": "Строительство, ремонт, производство",
        "src": "svg/orders/construction.svg"
    },

    {
        "id": 6,
        "name": "СМИ",
        "src": "svg/orders/media.svg"
    },

    {
        "id": 7,
        "name": "Разработка ПО",
        "src": "svg/orders/it.svg"
    },

    {
        "id": 8,
        "name": "Проектирование",
        "src": "svg/orders/engineering.svg"
    },

    {
        "id": 9,
        "name": "Дизайн",
        "src": "svg/orders/design.svg"
    },

    {
        "id": 10,
        "name": "Финансы и бухгалтерия",
        "src": "svg/orders/finance.svg"
    },

    {
        "id": 11,
        "name": "HoReCa",
        "src": "svg/orders/horeca.svg"
    },
    {
        "id": 12,
        "name": "Маркетинг",
        "src": "svg/orders/marketing.svg"
    },
    {
        "id": 13,
        "name": "Красота и здоровье",
        "src": "/svg/orders/beauty.svg"
    },
]

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
    } for i in range(150)
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
