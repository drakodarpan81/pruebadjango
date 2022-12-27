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
    descripcion_articulo = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = CatArticulo
        fields = ['nombre_articulo', 'descripcion_articulo', 'cantidad', 'presentacion', 'proveedor', 'imagen', 'estado', 'stock_minimo', ]
        summernote_fields = ('descripcion_articulo', )

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['cantidad'].widget.attrs['readonly'] = 'True'

    def clean(self):
        try:
            nombre_articulo = CatArticulo.objects.get(
                nombre_articulo=self.cleaned_data['nombre_articulo'].upper()
            )
            
            if not self.instance.pk:
                raise forms.ValidationError("[Nombre del artículo] = Este registro ya existe")
            elif self.instance.pk!=nombre_articulo.pk:
                raise forms.ValidationError("[Nombre del artículo] = Cambio no permitido, coincide con otro registro")

        except CatArticulo.DoesNotExist:
            pass

        if self.cleaned_data.get('descripcion_articulo', None) is None:
            raise forms.ValidationError("[Descripción artículo] = Es necesario capturar una descripción")

        return self.cleaned_data

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = CatProveedor
        fields = '__all__'

    def clean(self):
        try:
            nombre_proveedor = CatProveedor.objects.get(
                nombre_proveedor=self.cleaned_data['nombre_proveedor'].upper()
            )

            if not self.instance.pk:
                raise forms.ValidationError("[Nombre del proveedor] = Este registro ya existe")
            elif self.instance.pk!=nombre_proveedor.pk:
                raise forms.ValidationError("[Nombre del proveedor] = Cambio no permitido, coincide con otro registro")
        except CatProveedor.DoesNotExist:
            pass

        return self.cleaned_data
