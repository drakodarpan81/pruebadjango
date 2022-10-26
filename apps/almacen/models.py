from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CatPresentacion(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    descripcion = models.CharField(_("Descripción de la presentación"), max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = _("CatPresentacion")
        verbose_name_plural = _("CatPresentaciones")

    def __str__(self):
        return self.descripcion

    def get_absolute_url(self):
        return reverse("CatPresentacion_detail", kwargs={"pk": self.pk})

class CatCategoria(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    descripcion = models.CharField(_("Descripción de la categoría"), max_length=50, blank=True, null=True)
    

    class Meta:
        verbose_name = _("CatCategoria")
        verbose_name_plural = _("CatCategorias")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CatCategoria_detail", kwargs={"pk": self.pk})


class catalogomercancia(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    descripcion_producto = models.CharField(_("Descripción del producto"), max_length=100, blank=False, null=False)
    presentacion = models.ForeignKey(CatPresentacion, related_name='CatPresentaciones', on_delete=models.CASCADE)
    categorias = models.ForeignKey(CatCategoria, related_name='CatCategorias', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("catalogomercancia")
        verbose_name_plural = _("catalogomercancias")

    def __str__(self):
        return self.descripcion_producto

    def get_absolute_url(self):
        return reverse("catalogomercancia_detail", kwargs={"pk": self.pk})
