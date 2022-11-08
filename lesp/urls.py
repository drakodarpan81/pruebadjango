"""lesp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from apps.inicio.views import InicioView
from apps.login.views import *
from apps.home.views import HomeViews
from apps.almacen.views import *
from apps.catalogos.views import *
from apps.almacen.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',InicioView.as_view(), name="inicio"),

    # Login de USUARIOS
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginFormView.as_view(), name='login'),
    path('dashbord/', HomeViews.as_view(), name='dashbord'),
    path('logout/', logout_request, name='logout'),
    
    # Catalogos
    path('catalogos/presentacion', PresentacionView.as_view(), name='catalogo_presentacion'),
    path('catalogos/articulos', ArticuloView.as_view(), name='catalogo_articulos'),
    path('catalogos/proveedores', ProveedorView.as_view(), name='catalogo_proveedores'),

    # Listados
    path('catalogos/listado_articulos', ArticuloListView.as_view(), name='listado_articulos'),
    path('catalogos/listado_proveedores', ProveedoresListView.as_view(), name='listado_proveedores'),

    # Editar
    path('catalogos/edit_articulos/<int:pk>/', ArticuloUpdateView.as_view(), name='editar_articulos'),
    path('catalogos/edit_proveedor/<int:pk>/', ProveedorUpdateView.as_view(), name='editar_proveedor'),

    # Eliminar
    path('catalogos/delete_articulos/<int:pk>/', ArticuloDeleteView.as_view(), name='delete_articulos'),
    path('catalogos/delete_proveedor/<int:pk>/', ProveedorDeleteView.as_view(), name='delete_proveedor'),

    # Control de almacen
    #path('almacen/entradas', EntradasAlmacenViews.as_view(), name='entradas_almacen'),
    path('almacen/entradas', listar_articulos, name='entradas_almacen'),
    
    # Summernote
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)