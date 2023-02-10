from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CatUsuario(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre = models.CharField(_("Nombre del usuario"), max_length=50)
    apellido_paterno = models.CharField(_("Apellido paterno"), max_length=50)
    apellido_materno = models.CharField(_("Apellido materno"), max_length=50)
    fecha_alta = models.DateField(_("Fecha de ingreso"), auto_now_add=True)
    nota_buena = models.BooleanField(_("Buena / Mala"))
    cedula = models.PositiveIntegerField(_("Cédula"))
    email = models.EmailField(_("Email"), max_length=254)
    

    class Meta:
        verbose_name = _("CatUsuario")
        verbose_name_plural = _("CatUsuarios")

    def __str__(self):
        return "Usuario: {nombre} {apellido_paterno} {apellido_materno}".format(nombre=self.nombre, apellido_paterno=self.apellido_paterno, apellido_materno=self.apellido_materno)

