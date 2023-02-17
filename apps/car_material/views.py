from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.catalogos.models import CatArticulo

# Create your views here.
class Carrito(LoginRequiredMixin, ListView):
    model = CatArticulo
    template_name = "carrito.html"