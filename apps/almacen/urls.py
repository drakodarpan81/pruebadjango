from django.urls import path
from apps.almacen.views import *

urlpatterns = [
    # Control de almacen
    path('', entradasalmacen, name='opcion_almacen'),

    # Entradas al almacen
    path('entradas/<int:id_articulo>/', listar_articulos, name='entrada_almacen'),
    path('entradas/actualizar/<int:id_articulo>/', actualizar_articulo, name='actualizar_entrada_almacen'),

    # Salidas del almacen
    path('salidas/<int:id_articulo>/', salida_almacen, name='salida_almacen'),
    path('salidas/actualizar/<int:id_articulo>/', restar_inventario_articulo, name='actualizar_salida_almacen'),
]
