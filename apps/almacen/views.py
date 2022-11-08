from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Catálogo articulos
from apps.catalogos.models import CatArticulo

# Create your views here.
"""
class EntradasAlmacenViews(LoginRequiredMixin,ListView):
    template_name = "entradas_almacen.html"
    model = CatArticulo

    def get_queryset(self):
        buscar_articulo = self.GET.get("buscar_articulo")
        return CatArticulo.objects.filter(name = buscar_articulo)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_card"] = 'Entrada del almacen'
        context["icon_card"] = 'fa-solid fa-boxes-packing'
        return context
"""

def listar_articulos(request):
    buscar_articulo = request.GET.get("buscar_articulo")
    articulos = CatArticulo.objects.all()

    if buscar_articulo:
        articulos = CatArticulo.objects.filter(
            Q(nombre_articulo__icontains = buscar_articulo)
        ).distinct()

    return render(request, 'entradas_almacen.html', {'articulos':articulos} )
