from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords

# Create your models here.
class CatPersonalLaboratorio(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre_empleado = models.CharField(_("Nombre del empleado"), max_length=100, unique=True, blank=False)
    rfc = models.CharField(_("RFC"), max_length=15, unique=True, blank=False)
    email = models.EmailField(max_length=254,blank=True)
    fecha_ingreso = models.DateField(_("Fecha ingreso"), auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("CatPersonalLaboratorio")
        verbose_name_plural = _("CatPersonalLaboratorios")

    def __str__(self):
        return self.nombre_empleado

class CatPersonalEncargadoArea(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre_empleado = models.CharField(_("Nombre del empleado"), max_length=100, unique=True, blank=False)
    nombre_empleado_coordinador = models.ManyToManyField(CatPersonalLaboratorio, through='CatCoordinacion')
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("CatPersonalEncargadoArea")
        verbose_name_plural = _("CatPersonalEncargadoAreas")

    def __str__(self):
        return self.nombre_empleado


class CatCoordinacion(models.Model):
    """Model definition for CatCoordinacion."""
    COORDINACIONES = {
        ('0', 'Vigilancia Sanitaria'),
        ('1', 'Vigilancia Epidemiologica'),
        ('2', 'Administración'),
        ('3', 'Inovación y Gestión de Calidad')
    }

    id = models.AutoField(_("id"), primary_key=True)
    nombre_coordinacion = models.CharField(_("Nombre de la coordinación"), max_length=50, blank=False,unique=True)
    nombre_area = models.CharField(_("Nombre del área"), max_length=1, choices=COORDINACIONES)
    coordinador_responsable = models.ForeignKey(CatPersonalLaboratorio, related_name="CatPersonalLaboratorio", on_delete=models.CASCADE)
    responsable_area = models.ForeignKey(CatPersonalEncargadoArea, related_name="CatPersonalLaboratorio", on_delete=models.CASCADE)
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
