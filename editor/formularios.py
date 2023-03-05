from django import forms
from editor.models import Tipo_Tramite,Rol,Tipo_Documento, Estado


class FormularioTramite(forms.Form):
    nombre = forms.CharField(required=True)
    tiempo_estimado_dias = forms.CharField(required=True)
    estado = forms.ChoiceField(required=True,choices=((True,'Habilitado'),(False,'Deshabilitado')))
    opcionesRoles = [(choice.pk, choice.Rol) for choice in Rol.objects.raw('SELECT * FROM EDITOR_ROL')]
    rolesPermitidos = forms.MultipleChoiceField(label="Roles con permisos",required=True,choices=opcionesRoles,widget=forms.CheckboxSelectMultiple)
    opcionesDocumentos = [(choice.pk, choice.nombre) for choice in Tipo_Documento.objects.raw('SELECT * FROM EDITOR_TIPO_DOCUMENTO')]
    requerimientos = forms.MultipleChoiceField(label="Documentos requeridos para tramite",required=True,choices=opcionesDocumentos,widget=forms.CheckboxSelectMultiple)
    
    class meta:
        model = Tipo_Tramite


class Formulario_Estado(forms.Form):
    nombre = forms.CharField(required=True)

    class meta:
        model = Estado