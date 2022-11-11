from distutils.text_file import TextFile
from django import forms

# Modelos
from apps.catalogos.models import CatArticulo

class AlmacenArticulosForm(forms.ModelForm):
    
    class Meta:
        model = CatArticulo
        fields = ['imagen', 'nombre_articulo', 'cantidad', 'requisicion', 'fecha_entrada_almacen']

