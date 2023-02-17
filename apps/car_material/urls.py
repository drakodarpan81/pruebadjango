from django.urls import path
from apps.car_material.views import *

urlpatterns = [
    path('carro_materiales/', Carrito.as_view(), name='carrito'),
]