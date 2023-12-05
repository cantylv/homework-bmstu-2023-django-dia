from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # главная страница с кнопками
    path('services/<int:service_id>/', views.service, name='service'),  # страница заказа
]
