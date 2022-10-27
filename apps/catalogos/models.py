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

    def get_absolute_url(self):
        return reverse("CatPresentacion_detail", kwargs={"pk": self.pk})

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

    def get_absolute_url(self):
        return reverse("CatCategoria_detail", kwargs={"pk": self.pk})


class CatMercancia(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    descripcion_producto = models.CharField(_("Descripción del producto"), max_length=100, blank=False, unique=True)
    presentacion = models.ForeignKey(CatPresentacion, related_name='CatPresentaciones', on_delete=models.CASCADE)
    categorias = models.ForeignKey(CatCategoria, related_name='CatCategorias', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(_("Cantidad"))
    imagen = models.ImageField(_("Imagen del producto"), upload_to='mercancia/', blank=True, null=True, max_length=200)
    fecha_alta = models.DateTimeField(_("Fecha de alta de la mercancía"), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_("Fecha de modificación de la mercancía"), auto_now=True)

    class Meta:
        verbose_name = _("CatMercancia")
        verbose_name_plural = _("CatMercancias")

    def __str__(self):
        return self.descripcion_producto

    def get_absolute_url(self):
        return reverse("CatMercancia_detail", kwargs={"pk": self.pk})