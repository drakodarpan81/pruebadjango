from django.urls import path
from apps.catalogos.views import *

urlpatterns = [
    # Catalogos
    path('presentacion/', PresentacionView.as_view(),
         name='catalogo_presentacion'),
    path('articulos/', ArticuloView.as_view(), name='catalogo_articulos'),
    path('proveedores/', ProveedorView.as_view(),
         name='catalogo_proveedores'),

    # Listados
    path('listado_articulos/',
         ArticuloListView.as_view(), name='listado_articulos'),
    path('listado_proveedores/',
         ProveedoresListView.as_view(), name='listado_proveedores'),

    # Editar
    path('edit_articulos/<int:pk>/',
         ArticuloUpdateView.as_view(), name='editar_articulos'),
    path('edit_proveedor/<int:pk>/',
         ProveedorUpdateView.as_view(), name='editar_proveedor'),

    # Eliminar
    path('delete_articulos/<int:pk>/',
         ArticuloDeleteView.as_view(), name='delete_articulos'),
    path('delete_proveedor/<int:pk>/',
         ProveedorDeleteView.as_view(), name='delete_proveedor'),
]
