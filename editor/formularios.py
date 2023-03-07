from django import forms
from editor.templatetags.poll_extras import get_verbose_name
from editor.models import Tipo_Tramite,Rol,Tipo_Documento, Estado, Comentarios, Tipo_Archivo, Rol


class FormularioTramite(forms.ModelForm):
    nombre = forms.CharField(required=True)
    tiempo_estimado_dias = forms.CharField(required=True)
    estado = forms.ChoiceField(required=True,choices=((True,'Habilitado'),(False,'Deshabilitado')))
    opcionesRoles = [(choice.pk, choice.Rol) for choice in Rol.objects.raw('SELECT * FROM EDITOR_ROL')]
    rolesPermitidos = forms.MultipleChoiceField(label="Roles con permisos",required=True,choices=opcionesRoles,widget=forms.CheckboxSelectMultiple)
    opcionesDocumentos = [(choice.pk, choice.nombre) for choice in Tipo_Documento.objects.raw('SELECT * FROM EDITOR_TIPO_DOCUMENTO')]
    requerimientos = forms.MultipleChoiceField(label="Documentos requeridos para tramite",required=True,choices=opcionesDocumentos,widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Tipo_Tramite

        fields =[

        ]

class Formulario_Estado(forms.ModelForm):
    nombre = forms.CharField(required=True, label=get_verbose_name(Estado, 'nombre'))

    class Meta:
        model = Estado

        fields = [
            'nombre',
        ]

class Formulario_Comentario(forms.ModelForm):
    descr = forms.CharField(required=True, label=get_verbose_name(Comentarios, 'descr'))

    class Meta:
        model = Comentarios

        fields = [
            'descr',
        ]

class Formulario_Tipo_Archivo(forms.ModelForm):
    extension = forms.CharField(required=True, label=get_verbose_name(Tipo_Archivo, 'extension'))

    class Meta:
        model = Tipo_Archivo

        fields = [
            'extension',
        ]

class Formulario_Rol(forms.ModelForm):
    Rol = forms.CharField(required=True, label=get_verbose_name(Rol, 'Rol'))

    class Meta:
        model = Rol

        fields = [
            'Rol',
        ]