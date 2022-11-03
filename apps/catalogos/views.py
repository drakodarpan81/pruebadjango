from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.catalogos.models import CatPresentacion, CatArticulo, CatProveedor
from apps.catalogos.forms import PresentacionForm, ArticuloForm, ProveedorForm

# Create your views here.
class PresentacionView(LoginRequiredMixin, CreateView):
    model = CatPresentacion
    template_name = "presentacion.html"
    form_class = PresentacionForm
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación de una presentación'
        print(reverse_lazy('inicio'))
        return context

# CURD Articulos
class ArticuloView(LoginRequiredMixin, CreateView):
    model=CatArticulo
    template_name='articulos.html'
    form_class=ArticuloForm
    success_url=reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Alta de articulos'
        context["title_card"] = 'Alta de'
        context["icon_card"] = 'fa-solid fa-file-circle-plus'
        return context
    
class ArticuloListView(LoginRequiredMixin, ListView):
    model = CatArticulo
    template_name = "list_articulo.html"


class ArticuloUpdateView(LoginRequiredMixin,UpdateView):
    model = CatArticulo
    template_name = "articulos.html"
    form_class=ArticuloForm
    success_url=reverse_lazy('listado_articulos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar articulo'
        context["title_card"] = 'Actualización del'
        context["icon_card"] = 'fa-solid fa-pen-to-square'
        return context
    

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = CatArticulo
    template_name = "delete_articulo.html"
    success_url=reverse_lazy('listado_articulos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Borrado de articulos'
        context["icon_card"] = 'fa-solid fa-trash-can'
        context["list_url"] = reverse_lazy('listado_articulos')
        return context
    
# CURD Proveedores
class ProveedorView(LoginRequiredMixin, CreateView):
    model=CatProveedor
    template_name="proveedores.html"
    form_class=ProveedorForm
    success_url=reverse_lazy('inicio')

    """
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            print(request.POST)

        return render(request, self.template_name, {'form': form})
    """