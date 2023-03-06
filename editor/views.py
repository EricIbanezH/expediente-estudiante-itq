from email.policy import default
from django.shortcuts import render
from editor.formularios import FormularioTramite, Formulario_Estado, Formulario_Comentario, Formulario_Tipo_Archivo
from editor.models import Tipo_Archivo, Tipo_Documento, Tipo_Tramite, Estado, Rel_Tram_Doc, Rel_Tram_Rol,Rol, Comentarios

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

def publicarRelacionTramiteDocumento(modeloTipoTramite,listaIdDocumento):
    for documentoId in listaIdDocumento:
        modeloTipoDocumento = Tipo_Documento.objects.get(id=documentoId)
        nuevaRelacionTramiteDocumento = Rel_Tram_Doc(
            tramite=modeloTipoTramite,
            documento= modeloTipoDocumento
        )
        nuevaRelacionTramiteDocumento.save()

def publicarRelacionTramiteRol(modeloTipoTramite,listaIdRoles):
    for rolId in listaIdRoles:
        modeloRol = Rol.objects.get(id=rolId)
        nuevaRelacionTramiteRol = Rel_Tram_Rol(
            tramite=modeloTipoTramite,
            rol=modeloRol
        )
        nuevaRelacionTramiteRol.save()

def publicarTipoTramite(request):
    nuevoTipoTramite = Tipo_Tramite(
        nombre=request.POST['nombre'],
        tiempo_estimado=request.POST['tiempo_estimado_dias'],
        habilitado=request.POST['estado']
        )
    nuevoTipoTramite.save()
    
    listaIdDeRoles = request.POST.getlist('rolesPermitidos',default=['emptyList'])
    publicarRelacionTramiteRol(nuevoTipoTramite,listaIdDeRoles)
    listaIdDeDocumentos = request.POST.getlist('requerimientos',default=['emptyList'])
    publicarRelacionTramiteDocumento(nuevoTipoTramite,listaIdDeDocumentos)

def crearTipoTramite(request):
    if request.method=='GET':
        contexto = {'form': FormularioTramite}
        return render(request,'formulario.html',contexto)
    else:
        publicarTipoTramite(request)
        return render(request,'index.html')
    
def listarTipoDeTramites(request):
    if request.method=='GET':
        contexto = {'listaTipoDeTramites':Tipo_Tramite.objects.all(),
                    'listaRelacionTramiteRol': Rel_Tram_Rol.objects.all()}
        return render(request,'lista-tipo-de-tramite.html',contexto)

           
# Create your views here.
# R: nel

# Vistas de los Estados
def crear_Estado(request):
    if request.method=='GET':
        contexto = {'form': Formulario_Estado}
        return render(request,'formulario.html',contexto)
    else:
        nuevoRegistro = Estado(
            nombre = request.POST['nombre']
        )
        nuevoRegistro.save()
        return render(request,'index.html')
    
def listar_Estados(request):
    lista = Estado.objects.all()
    return render(request, 'listas/lista-estado.html', {'object_list' : lista})

class editar_Estado(UpdateView):
    model = Estado
    form_class = Formulario_Estado
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_estados')

# Vistas de los Comentarios
def crear_Comentario(request):
    if request.method=='GET':
        contexto = {'form': Formulario_Comentario}
        return render(request,'formulario.html',contexto)
    else:
        nuevoRegistro = Comentarios(
            descr = request.POST['descr']
        )
        nuevoRegistro.save()
        return render(request,'index.html')
    
def listar_Comentarios(request):
    lista = Comentarios.objects.all()
    return render(request, 'listas/lista-comentario.html', {'object_list' : lista})

class editar_Comentario(UpdateView):
    model = Comentarios
    form_class = Formulario_Comentario
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_comentarios')

# Vistas de los tipo-archivo
def crear_Tipo_Archivo(request):
    if request.method=='GET':
        contexto = {'form': Formulario_Tipo_Archivo}
        return render(request,'formulario.html',contexto)
    else:
        nuevoRegistro = Tipo_Archivo(
            extension = request.POST['extension']
        )
        nuevoRegistro.save()
        return render(request,'index.html')
    
def listar_Tipo_Archivos(request):
    lista = Tipo_Archivo.objects.all()
    return render(request, 'listas/lista-tipo-archivo.html', {'object_list' : lista})

class editar_Tipo_Archivo(UpdateView):
    model = Tipo_Archivo
    form_class = Formulario_Tipo_Archivo
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_tipo_archivos')