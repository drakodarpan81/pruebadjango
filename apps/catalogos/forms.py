from distutils.text_file import TextFile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from distutils.command.clean import clean
from django import forms
from apps.catalogos.models import CatPresentacion, CatArticulo, CatProveedor

class PresentacionForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = CatPresentacion
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    descripcion_articulo = forms.CharField(widget=SummernoteWidget())

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = CatArticulo
        fields = '__all__'
        summernote_fields = ('descripcion_articulo', 'observacion',)


class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = CatProveedor
        fields = '__all__'
