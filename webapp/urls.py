from django.urls import path
from . import views

# нужно обработать неправильные input-ы в get-параметрах

urlpatterns = [
    path('', views.home, name='home'),  # главная страница с кнопками
    path('catalog/orders', views.orders, name='orders'),  # страница с заказами
    path('catalog/orders/<int:order_id>/', views.order, name='order'),  # страница заказа

    path('executors/', views.executors, name='executors'),  # главная страница с кнопками
    path('executors/contractors', views.contractors, name='contractors'),  # страница с исполнителями
    path('executors/contractors/<int:contractor_id>/', views.contractor, name='contractor'),  # страница исполнителя
]
