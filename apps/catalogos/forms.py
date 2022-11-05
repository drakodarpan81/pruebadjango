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
        fields = ['nombre_articulo', 'descripcion_articulo', 'cantidad', 'presentacion', 'proveedor', 'imagen', 'estado', 'observacion',]
        summernote_fields = ('descripcion_articulo', )

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['cantidad'].widget.attrs['readonly'] = 'True'

    def clean(self):
        try:
            campo = CatArticulo.objects.get(
                nombre_articulo=self.cleaned_data['nombre_articulo'].upper()
            )

            if not self.instance.pk:
                raise forms.ValidationError("[Nombre del artículo] = Este registro ya existe")
            elif self.instance.pk!=campo.pk:
                raise forms.ValidationError("[Nombre del artículo] = Cambio no permitido, coincide con otro registro")
        except CatArticulo.DoesNotExist:
            pass
        return self.cleaned_data

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = CatProveedor
        fields = '__all__'
