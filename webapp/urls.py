from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('executors/', views.executors, name='executors'),
    path('executors/contractors', views.contractors, name='contractors'),
    path('catalog/orders', views.orders, name='orders'),
]
