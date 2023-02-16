from django.db import models
from simple_history.models import HistoricalRecords

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
    rfc = models.CharField(_("RFC"), max_length=15, unique=True, blank=False, default="#")
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("CatUsuario")
        verbose_name_plural = _("CatUsuarios")

    def __str__(self):
        return "Usuario: {nombre} {apellido_paterno} {apellido_materno}".format(nombre=self.nombre, apellido_paterno=self.apellido_paterno, apellido_materno=self.apellido_materno)

"""
# Encargado de área, cuando el coordinador no se encuentra
class CatPersonalEncargadoArea(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre_empleado = models.CharField(_("Nombre del empleado"), max_length=100, unique=True, blank=False)
    nombre_empleado_coordinador = models.ManyToManyField(CatUsuario, through='CatCoordinacion')
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("CatPersonalEncargadoArea")
        verbose_name_plural = _("CatPersonalEncargadoAreas")

    def __str__(self):
        return self.nombre_empleado
"""

class CatCoordinacion(models.Model):
    """Model definition for CatCoordinacion."""
    COORDINACIONES = {
        ('0', 'VIGILANCIA SANITARIA'),
        ('1', 'VIGILANCIA EPIDEMIOLOGICA'),
        ('2', 'ADMINISTRACIÓN'),
        ('3', 'INOVACIÓN Y GESTIÓN DE CALIDAD')
    }

    id = models.AutoField(_("id"), primary_key=True)
    nombre_coordinacion = models.CharField(_("Nombre de la coordinación"), max_length=50, blank=False,unique=True)
    nombre_area = models.CharField(_("Nombre del área"), max_length=1, choices=COORDINACIONES)
    coordinador_responsable = models.ForeignKey(CatUsuario, related_name="CatPersonalLaboratorio", on_delete=models.CASCADE)
    # responsable_area = models.ForeignKey(CatPersonalEncargadoArea, related_name="CatPersonalLaboratorio", on_delete=models.CASCADE)
    estado = models.BooleanField(_("Activo / Inactivo"), default=True)
    fecha_alta = models.DateField(_("Fecha alta"), auto_now_add=True)
    fecha_modificacion = models.DateTimeField(_("Fecha modificacion"), auto_now=True)
    history = HistoricalRecords()

    class Meta:
        """Meta definition for CatCoordinacion."""
        verbose_name = 'CatCoordinacion'
        verbose_name_plural = 'CatCoordinaciones'

    def __str__(self):
        """Unicode representation of CatCoordinacion."""
        return self.nombre_coordinacion
