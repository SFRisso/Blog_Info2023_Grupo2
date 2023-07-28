from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields=["usuario","titulo","contenido","localidad","imagen_portada","modalidad","categoria"]
