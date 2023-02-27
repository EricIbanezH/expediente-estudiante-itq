from django import forms
from editor.models import Tipo_Tramite


class FormularioTramite(forms.ModelForm):
    nombre = forms.CharField(required=True)
    tiempo_estimado_dias = forms.CharField(required=True)
    habilitado = forms.ChoiceField(required=True,choices=(('Habilitar',True),('Deshabilitar',False)))
    class meta:
        model = Tipo_Tramite


