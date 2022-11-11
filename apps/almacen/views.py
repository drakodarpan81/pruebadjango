from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from django.db.models import Q

# Catálogo articulos
from apps.catalogos.models import CatArticulo
from .forms import AlmacenArticulosForm

# Create your views here.

class EntradasAlmacenViews(LoginRequiredMixin,ListView):
    template_name = "manejo_almacen.html"
    model = CatArticulo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_card"] = 'Manejo del almacen'
        context["icon_card"] = 'fa-solid fa-person-military-to-person'
        return context


def listar_articulos(request, id_articulo):
    articulos = CatArticulo.objects.filter(id=id_articulo).first()
    form = AlmacenArticulosForm(instance=articulos)

    return render(request, 'entradas_almacen_Old.html', {'form':form, 'articulos':articulos} )


