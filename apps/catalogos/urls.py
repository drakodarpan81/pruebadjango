from django.urls import path
from apps.catalogos.views import *

urlpatterns = [
    # Catalogos
    path('catalogos/presentacion', PresentacionView.as_view(),
         name='catalogo_presentacion'),
    path('catalogos/articulos', ArticuloView.as_view(), name='catalogo_articulos'),
    path('catalogos/proveedores', ProveedorView.as_view(),
         name='catalogo_proveedores'),

    # Listados
    path('catalogos/listado_articulos',
         ArticuloListView.as_view(), name='listado_articulos'),
    path('catalogos/listado_proveedores',
         ProveedoresListView.as_view(), name='listado_proveedores'),

    # Editar
    path('catalogos/edit_articulos/<int:pk>/',
         ArticuloUpdateView.as_view(), name='editar_articulos'),
    path('catalogos/edit_proveedor/<int:pk>/',
         ProveedorUpdateView.as_view(), name='editar_proveedor'),

    # Eliminar
    path('catalogos/delete_articulos/<int:pk>/',
         ArticuloDeleteView.as_view(), name='delete_articulos'),
    path('catalogos/delete_proveedor/<int:pk>/',
         ProveedorDeleteView.as_view(), name='delete_proveedor'),
]
