# Локальная база данных

import random

# УСЛУГИ

JOBS = [
    'Программист 1С',
    'Специалист по массажу',
    'Сантехник',
    'Мастер по чистке салона автомобиля',
    'Ветеринар',
    'Окулист',
    'Уролог',
    'Гинеколог',
    'Репетитор по математике',
    'Юрист',
    'Охранник',
    'Аналитик данных',
    'Финансовый консультант',
    'Тренер по боксу',
    'Фитнес тренер',
    'Стилист',
    'Фотограф',
]

SERVICES = [
    {
        'id': i,
        'job': job,
        'img': 'img/user1.jpg',
        'about': f'you can to do {i}',
        'age': random.randint(20, 35),
        'sex': random.randint(0, 2),  # 0 - women, 1 - men, 2 - man and woman
        'rus_passport': random.randint(0, 1),
        'insurance': random.randint(0, 1),
    } for i, job in enumerate(random.sample(JOBS, 10))
]