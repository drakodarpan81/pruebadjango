from datetime import datetime
from django.shortcuts import render
# from django.db.models import Q

# Catálogo articulos
from apps.catalogos.models import CatArticulo
from .forms import AlmacenArticulosForm

# Create your views here.
def entradasalmacen(request):
    articulos = CatArticulo.objects.all()
    return render(request, "manejo_almacen.html", {'articulos':articulos})

def listar_articulos(request, id_articulo):
    articulos = CatArticulo.objects.filter(id=id_articulo).first()
    form = AlmacenArticulosForm(instance=articulos)
 
    return render(request, 'entradas_almacen_Old.html', {'form':form, 'articulos':articulos} )

def actualizar_articulo(request, id_articulo):
    dFechaEntrada = request.POST["fecha_entrada_almacen"]
    fecha_entrada = datetime.strptime(dFechaEntrada, "%d/%m/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
    nCantidad = int(request.POST["cantidad"])
    sRequisicion = request.POST["requisicion"]
    id = int(request.POST["id"])

    articulo = CatArticulo.objects.get(id=id)
    articulo.fecha_entrada_almacen = fecha_entrada
    articulo.cantidad = articulo.cantidad + nCantidad
    articulo.requisicion = sRequisicion
    articulo.save()
    
    articulos = CatArticulo.objects.all()
    return render(request, 'manejo_almacen.html', {'articulos':articulos})