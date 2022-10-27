from django.forms import *
from apps.catalogos.models import CatPresentacion

class PresentacionForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = CatPresentacion
        fields = '__all__'
        widgets = {
            'nombre_presentacion': TextInput(
                attrs={
                    'placeholder': 'Ingresa un tipo de presentación',
                    'class':'form-control',
                    'autocomplete': 'off',
                    'autofocus': True
                }
            )
        }