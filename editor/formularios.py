from django import forms
from editor.templatetags.poll_extras import get_verbose_name
from editor.models import Tipo_Tramite,Rol,Tipo_Documento, Estado, Comentarios, Tipo_Archivo, Rol


class FormularioTramite(forms.ModelForm):
    opcionesRoles = [(choice.pk, choice.Rol) for choice in Rol.objects.raw('SELECT * FROM EDITOR_ROL')]
    rolesPermitidos = forms.MultipleChoiceField(label="Roles con permisos",required=True,choices=opcionesRoles,widget=forms.CheckboxSelectMultiple)
    opcionesDocumentos = [(choice.pk, choice.nombre) for choice in Tipo_Documento.objects.raw('SELECT * FROM EDITOR_TIPO_DOCUMENTO')]
    requerimientos = forms.MultipleChoiceField(label="Documentos requeridos para tramite",required=True,choices=opcionesDocumentos,widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Tipo_Tramite

        fields =[
            'nombre','tiempo_estimado','habilitado'
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

class Formulario_tipoDocumento(forms.ModelForm):
    nombre = forms.CharField(required=True, label=get_verbose_name(Tipo_Documento, 'nombre'))
    tamano_MB = forms.IntegerField(required=True, label=get_verbose_name(Tipo_Documento, 'tamano_MB'))
    listaExtensiones = [(choice.pk, choice.extension) for choice in Tipo_Archivo.objects.raw('SELECT * FROM EDITOR_TIPO_ARCHIVO')]
    tipo_archivo = forms.ChoiceField(label="Extension del documento",required=True,choices=listaExtensiones)
    
    class Meta:
        model = Tipo_Documento

        fields = [
            'nombre',
            'tamano_MB',
        ]

