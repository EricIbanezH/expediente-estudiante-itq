from django import forms
from editor.templatetags.poll_extras import get_verbose_name
from editor.models import Tipo_Tramites, Rol, Tipo_Documentos, Estados, Comentarios, Tipo_Archivos


class FormularioTramite(forms.ModelForm):
    opcionesRoles = [(choice.pk, choice.Rol) for choice in Rol.objects.raw('SELECT * FROM EDITOR_ROL')]
    rolesPermitidos = forms.MultipleChoiceField(label="Roles con permisos",required=True,choices=opcionesRoles,widget=forms.CheckboxSelectMultiple)
    opcionesDocumentos = [(choice.pk, choice.nombre) for choice in Tipo_Documentos.objects.all()]
    requerimientos = forms.MultipleChoiceField(label="Documentos requeridos para tramite",required=True,choices=opcionesDocumentos,widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Tipo_Tramites

        fields =[
            'nombre','tiempo_estimado','habilitado'
        ]

class Formulario_Estado(forms.ModelForm):
    nombre = forms.CharField(required=True, label=get_verbose_name(Estados, 'nombre'))

    class Meta:
        model = Estados

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
    extension = forms.CharField(required=True, label=get_verbose_name(Tipo_Archivos, 'extension'))

    class Meta:
        model = Tipo_Archivos

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
    nombre = forms.CharField(required=True, label=get_verbose_name(Tipo_Documentos, 'nombre'))
    tamano_MB = forms.IntegerField(required=True, label=get_verbose_name(Tipo_Documentos, 'tamano_MB'))
    listaExtensiones = [(choice.pk, choice.extension) for choice in Tipo_Archivos.objects.all()]
    tipo_archivo = forms.ChoiceField(label="Extension del documento",required=True,choices=listaExtensiones)
    
    class Meta:
        model = Tipo_Documentos

        fields = [
            'nombre',
            'tamano_MB',
        ]

