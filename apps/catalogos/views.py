from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.catalogos.models import CatPresentacion, CatArticulo
from apps.catalogos.forms import PresentacionForm, ArticuloForm

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

class ArticuloView(LoginRequiredMixin, CreateView):
    model=CatArticulo
    template_name='articulos.html'
    form_class=ArticuloForm
    success_url=reverse_lazy('inicio')