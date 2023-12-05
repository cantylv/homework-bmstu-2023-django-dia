# Локальная база данных

import random

# УСЛУГИ

JOBS = [
    {
        'name': 'Программист 1С',
        'img': 'img/professions/prog.jpg'
    },
    {
        'name': 'Специалист по массажу',
        'img': 'img/professions/massage.jpg'
    },
    {
        'name': 'Сантехник',
        'img': 'img/professions/santechnik.jpg'
    },
    {
        'name': 'Мастер по чистке салона автомобиля',
        'img': 'img/professions/wash_car.jpg'
    },
    {
        'name': 'Ветеринар',
        'img': 'img/professions/veterinar.jpg'
    },
    {
        'name': 'Окулист',
        'img': 'img/professions/okulist.jpg'
    },
    {
        'name': 'Уролог',
        'img': 'img/professions/urolog.jpg'
    },
    {
        'name': 'Гинеколог',
        'img': 'img/professions/ginekolog.jpg'
    },
    {
        'name': 'Репетитор по математике',
        'img': 'img/professions/teacher.jpg'
    },
    {
        'name': 'Юрист',
        'img': 'img/professions/jurist.jpg'
    },
    {
        'name': 'Охранник',
        'img': 'img/professions/security.jpg'
    },
    {
        'name': 'Аналитик данных',
        'img': 'img/professions/datanal.jpg'
    },
    {
        'name': 'Финансовый консультант',
        'img': 'img/professions/consultant_money.jpg'
    },
    {
        'name': 'Тренер по боксу',
        'img': 'img/professions/traner_box.jpg'
    },
    {
        'name': 'Фитнес тренер',
        'img': 'img/professions/fitness.jpg'
    },
    {
        'name': 'Стилист',
        'img': 'img/professions/styleman.jpg'
    },
    {
        'name': 'Фотограф',
        'img': 'img/professions/photographer.jpg'
    }
]

SERVICES = [
    {
        'id': i,
        'job': job['name'],
        'img': job['img'],
        'about': f'you can to do {i}',
        'age': random.randint(20, 35),
        'sex': random.randint(0, 2),  # 0 - women, 1 - men, 2 - man and woman
        'rus_passport': random.randint(0, 1),
        'insurance': random.randint(0, 1),
    } for i, job in enumerate(random.sample(JOBS, 10))
]
