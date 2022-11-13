from django.urls import path
from apps.almacen.views import *

urlpatterns = [
    # Control de almacen
    path('almacen/', entradasalmacen, name='opcion_almacen'),
    path('almacen/entradas/<int:id_articulo>',
         listar_articulos, name='entrada_almacen'),
    path('almacen/entradas/actualizar/<int:id_articulo>',
         actualizar_articulo, name='actualizar_entrada_almacen'),
]
