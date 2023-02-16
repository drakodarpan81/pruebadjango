from django.urls import path
from apps.car_material.views import *

urlpatterns = [
    path('carro_materiales/', carrito, name='carrito'),
]