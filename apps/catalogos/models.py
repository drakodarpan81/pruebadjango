from distutils import text_file
from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CatPresentacion(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre_presentacion = models.CharField(_("Tipo de presentación"), max_length=50, blank=False, unique=True)
    fecha_alta = models.DateTimeField(_("Fecha de alta de la presentación"), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_("Fecha de modificación de la presentación"), auto_now=True)

    class Meta:
        verbose_name = _("CatPresentacion")
        verbose_name_plural = _("CatPresentaciones")

    def __str__(self):
        return self.nombre_presentacion

class CatCategoria(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre_categoria = models.CharField(_("Nombre de la categoría"), max_length=50, blank=False, unique=True)
    fecha_alta = models.DateTimeField(_("Fecha de alta de la categoría"), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_("Fecha de modificación de la categoría"), auto_now=True)

    class Meta:
        verbose_name = _("CatCategoria")
        verbose_name_plural = _("CatCategorias")

    def __str__(self):
        return self.nombre_categoria


class CatProveedor(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre_proveedor = models.CharField(_("Nombre del proveedor"), max_length=50, blank=False)
    rfc_proveedor = models.CharField(_("RFC"), max_length = 15, blank=False, unique=True)
    calle = models.CharField(_("Calles"), max_length=50, blank=True, null=True)
    numero = models.PositiveIntegerField(_("Número"))
    colonia = models.CharField(_("Colonia"), max_length=50, blank=True, null=True)
    codigo_postal = models.PositiveIntegerField(_("CP"))
    telefono = models.CharField(_("Teléfono"), max_length=15, blank=True, null=True)
    requisicion = models.CharField(_("Requisición"), max_length = 30, blank=False, unique=True)
    estado = models.BooleanField(_("Activo / Inactivo"), default=True)
    fecha_alta = models.DateTimeField(_("Fecha de alta de la mercancía"), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_("Fecha de modificación de la mercancía"), auto_now=True)

    class Meta:
        verbose_name = _("CatProveedor")
        verbose_name_plural = _("CatProveedores")

    def __str__(self):
        return self.nombre_proveedor


class CatArticulo(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre_articulo = models.CharField(_("Nombre del artículo"), max_length=50, blank=False, unique=True)
    descripcion_articulo = models.TextField()
    cantidad = models.PositiveIntegerField(_("Cantidad"))
    presentacion = models.ForeignKey(CatPresentacion, related_name='CatPresentaciones', on_delete=models.CASCADE)
    proveedor = models.ForeignKey(CatProveedor, related_name='CatProveedor', on_delete=models.CASCADE)
    imagen = models.ImageField(_("Imagen del producto"), upload_to='articulos/', blank=True, null=True, max_length=200)
    estado = models.BooleanField(_("Activo / Inactivo"), default=True)
    observacion = models.TextField(_("Observación"))
    fecha_alta = models.DateTimeField(_("Fecha de alta de la mercancía"), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_("Fecha de modificación de la mercancía"), auto_now=True)

    class Meta:
        verbose_name = _("CatArticulo")
        verbose_name_plural = _("CatArticulos")

    def __str__(self):
        return 'Articulo {} del proveedor {}'.format(self.nombre_articulo, self.proveedor.nombre_proveedor)
