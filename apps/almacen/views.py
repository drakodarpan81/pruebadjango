from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags

# Catálogo articulos
from apps.catalogos.models import CatArticulo
from .forms import AlmacenArticulosForm

# Create your views here.
@login_required
def entradasalmacen(request):
    articulos = CatArticulo.objects.all()
    return render(request, "manejo_almacen.html", {'articulos':articulos})

@login_required
def listar_articulos(request, id_articulo):
    articulos = CatArticulo.objects.filter(id=id_articulo).first()
    form = AlmacenArticulosForm(instance=articulos)
    return render(request, 'entradas_almacen.html', {'form':form, 'articulos':articulos} )

@login_required
def actualizar_articulo(request, id_articulo):
    dFechaEntrada = request.POST["fecha_entrada_almacen"]
    dFechaEntrada = dFechaEntrada.replace(",", "")
    if len(dFechaEntrada) > 16:
        dFechaEntrada = dFechaEntrada[:16]

    fecha_entrada = datetime.strptime(dFechaEntrada, "%d/%m/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
    nCantidad = int(request.POST["cantidad"])
    sRequisicion = request.POST["requisicion"]
    id = int(request.POST["id"])

    articulo = CatArticulo.objects.get(id=id)
    articulo.fecha_entrada_almacen = fecha_entrada
    articulo.cantidad = articulo.cantidad + nCantidad
    articulo.requisicion = sRequisicion
    articulo.save()
    messages.add_message(request=request, level=messages.SUCCESS, message="Se actualizo correctamente el inventario del articulo.")
    
    articulos = CatArticulo.objects.all()
    return render(request, 'manejo_almacen.html', {'articulos':articulos})

@login_required
def salida_almacen(request, id_articulo):
    articulos = CatArticulo.objects.filter(id=id_articulo).first()
    form = AlmacenArticulosForm(instance=articulos)
    return render(request, 'salidas_almacen.html', {'form':form, 'articulos':articulos} )
 
@login_required
def restar_inventario_articulo(request, id_articulo):
    dFechaSalida = request.POST["fecha_salida_almacen"]
    dFechaSalida = dFechaSalida.replace(",", "")
    if len(dFechaSalida) > 16:
        dFechaSalida = dFechaSalida[:16]

    fecha_salida = datetime.strptime(dFechaSalida, "%d/%m/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
    nCantidad = int(request.POST["cantidad"])
    sObservacion = request.POST["observacion"]
    id = int(request.POST["id"])

    articulo = CatArticulo.objects.get(id=id)
    articulo.fecha_salida_almacen = fecha_salida
    articulo.observacion = sObservacion

    if nCantidad > articulo.cantidad:
        articulos = CatArticulo.objects.filter(id=id_articulo).first()
        form = AlmacenArticulosForm(instance=articulos)
        messages.add_message(request=request, level=messages.ERROR, message="La [ CANTIDAD ] solicitada, es mayor a la cantidad con la que se cuenta en almacen.")
        return render(request, 'salidas_almacen.html', {'form':form, 'articulos':articulos} )
    else:
        articulo.cantidad = articulo.cantidad - nCantidad
        articulo.save()

        if articulo.cantidad < articulo.stock_minimo:
            enviarCorreo(articulo.descripcion_articulo)

        messages.add_message(request=request, level=messages.SUCCESS, message="Se actualizo correctamente el inventario del articulo.")
    
    articulos = CatArticulo.objects.all()
    return render(request, 'manejo_almacen.html', {'articulos':articulos})

def enviarCorreo(descripcion_articulo):
    # email_almacen.html
    template = get_template('email/email_almacen.html')
    content = template.render({
        'descripcion_articulo': strip_tags(descripcion_articulo),
    })

    msg = EmailMultiAlternatives(
        "Articulo agotado",
        'Artículo bajo de stock',
        settings.EMAIL_HOST_USER,
        ['drakodarpan@gmail.com']
    )

    msg.attach_alternative(content, 'text/html')
    msg.send()