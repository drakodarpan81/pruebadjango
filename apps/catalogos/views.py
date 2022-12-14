from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from apps.catalogos.models import CatPresentacion, CatArticulo, CatProveedor
from apps.catalogos.forms import PresentacionForm, ArticuloForm, ProveedorForm

# Create your views here.
class PresentacionView(LoginRequiredMixin, CreateView):
    model = CatPresentacion
    template_name = "presentacion.html"
    form_class = PresentacionForm
    success_url = reverse_lazy('dashbord')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación de una presentación'
        print(reverse_lazy('dashbord'))
        return context

# CURD Articulos
class ArticuloView(LoginRequiredMixin, CreateView):
    model=CatArticulo
    template_name='articulos/articulos.html'
    form_class=ArticuloForm
    success_url=reverse_lazy('listado_articulos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Alta de articulos'
        context["title_card"] = 'Alta de'
        context["icon_card"] = 'fa-solid fa-vial-circle-check'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'El articulo se dio de alta con éxito')
        return super().form_valid(form)

class ArticuloListView(LoginRequiredMixin, ListView):
    model = CatArticulo
    template_name = "articulos/list_articulo.html"


class ArticuloUpdateView(LoginRequiredMixin,UpdateView):
    model = CatArticulo
    template_name = "articulos/articulos.html"
    form_class=ArticuloForm
    success_url=reverse_lazy('listado_articulos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar articulo'
        context["title_card"] = 'Actualización del'
        context["icon_card"] = 'fa-solid fa-pen-to-square'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'El articulo se actualizo con éxito')
        return super().form_valid(form)
    

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = CatArticulo
    template_name = "articulos/delete_articulo.html"
    success_url=reverse_lazy('listado_articulos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Borrado de articulos'
        context["icon_card"] = 'fa-solid fa-trash-can'
        context["list_url"] = reverse_lazy('listado_articulos')
        return context
    
# CRUD Proveedores
class ProveedorView(LoginRequiredMixin, CreateView):
    model=CatProveedor
    template_name="proveedores/proveedores.html"
    form_class=ProveedorForm
    success_url=reverse_lazy('listado_proveedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Alta de proveedores'
        context["title_card"] = 'Alta de'
        context["icon_card"] = 'fa-solid fa-user-plus'
        context["subcategoria"] = 'Alta de proveedores'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'El proveedor se dio de alta con éxito')
        return super().form_valid(form)

class ProveedoresListView(LoginRequiredMixin, ListView):
    model = CatProveedor
    template_name = "proveedores/listado_proveedores.html"


class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = CatProveedor
    template_name = "proveedores/proveedores.html"
    form_class=ProveedorForm
    success_url=reverse_lazy('listado_proveedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualización de proveedores'
        context["title_card"] = 'Actualización de'
        context["icon_card"] = 'fa-solid fa-pen-to-square'
        context["subcategoria"] = 'Actualización de proveedores'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'El proveedor se actualizo con éxito')
        return super().form_valid(form)


class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = CatProveedor
    template_name = "proveedores/delete_proveedor.html"
    success_url = reverse_lazy('listado_proveedores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_url"] = reverse_lazy('listado_proveedores')
        return context
    