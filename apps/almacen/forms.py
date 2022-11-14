from distutils.text_file import TextFile
from django import forms
from django.contrib.admin import widgets

# Modelos
from apps.catalogos.models import CatArticulo

class AlmacenArticulosForm(forms.ModelForm):
    
    class Meta:
        model = CatArticulo
        fields = ['imagen', 'nombre_articulo', 'cantidad', 'requisicion', 'fecha_entrada_almacen', 'fecha_salida_almacen']

    def __init__(self, *args, **kwargs):
        super(AlmacenArticulosForm, self).__init__(*args, **kwargs)
        self.fields['fecha_entrada_almacen'].widget.attrs['readonly'] = True
        self.fields['fecha_salida_almacen'].widget.attrs['readonly'] = True