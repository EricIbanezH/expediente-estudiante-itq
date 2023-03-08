from email.policy import default
from django.shortcuts import render, redirect, get_object_or_404
from editor.formularios import FormularioTramite, Formulario_Estado, Formulario_Comentario, Formulario_Tipo_Archivo, Formulario_Rol
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
                    'listaRelacionTramiteRol': Rel_Tram_Rol.objects.all(),
                    'listaRelacionTramiteDocumentos': Rel_Tram_Doc.objects.all()}
        return render(request,'lista-tipo-de-tramite.html',contexto)

def eliminarRelacionTramiteRol(modeloTramite):
    relaciones = Rel_Tram_Rol.objects.filter(tramite=modeloTramite)
    for relacion in relaciones:
        relacion.delete()

def eliminarRelacionTramiteDocumento(modeloTramite):
    relaciones = Rel_Tram_Doc.objects.filter(tramite=modeloTramite)
    for relacion in relaciones:
        relacion.delete()    
    
class editar_tipoTramite(UpdateView):
    model = Tipo_Tramite
    form_class = FormularioTramite
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_tramites') 
    
    def post(self, request, *args, **kwargs):
     response = super().get(request, *args, **kwargs)
     
     eliminarRelacionTramiteRol(self.object)
     listaIdDeRoles = request.POST.getlist('rolesPermitidos',default=['emptyList'])
     publicarRelacionTramiteRol(self.object,listaIdDeRoles)
     
     eliminarRelacionTramiteDocumento(self.object)
     listaIdDeDocumentos = request.POST.getlist('requerimientos',default=['emptyList'])
     publicarRelacionTramiteDocumento(self.object,listaIdDeDocumentos)
     
     return super(editar_tipoTramite, self).post(request, **kwargs)

def eliminar_TipoTramite(request, pk):
    registro = get_object_or_404(Tipo_Tramite, id=pk)
    registro.delete()
    return redirect('listar_tramites')

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
        return redirect(request,'listar_estados')
    
def listar_Estados(request):
    lista = Estado.objects.all()
    return render(request, 'listas/lista-estado.html', {'object_list' : lista})

class editar_Estado(UpdateView):
    model = Estado
    form_class = Formulario_Estado
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_estados')

def eliminar_Estado(request, pk):
    registro = get_object_or_404(Estado, id=pk)
    registro.delete()
    return redirect('listar_estados')

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
        return redirect(request,'listar_comentarios')
    
def listar_Comentarios(request):
    lista = Comentarios.objects.all()
    return render(request, 'listas/lista-comentario.html', {'object_list' : lista})

class editar_Comentario(UpdateView):
    model = Comentarios
    form_class = Formulario_Comentario
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_comentarios')

def eliminar_Comentario(request, pk):
    registro = get_object_or_404(Comentarios, id=pk)
    registro.delete()
    return redirect('listar_comentarios')

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
        return redirect(request,'listar_tipo_archivos')
    
def listar_Tipo_Archivos(request):
    lista = Tipo_Archivo.objects.all()
    return render(request, 'listas/lista-tipo-archivo.html', {'object_list' : lista})

class editar_Tipo_Archivo(UpdateView):
    model = Tipo_Archivo
    form_class = Formulario_Tipo_Archivo
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_tipo_archivos')

def eliminar_Tipo_Archivo(request, pk):
    registro = get_object_or_404(Tipo_Archivo, id=pk)
    registro.delete()
    return redirect('listar_tipo_archivos')

# Vistas de los Roles
def crear_Rol(request):
    if request.method=='GET':
        contexto = {'form': Formulario_Rol}
        return render(request,'formulario.html',contexto)
    else:
        nuevoRegistro = Rol(
            Rol = request.POST['Rol']
        )
        nuevoRegistro.save()
        return redirect('listar_roles')
    
def listar_Roles(request):
    lista = Rol.objects.all()
    return render(request, 'listas/lista-roles.html', {'object_list' : lista})

class editar_Rol(UpdateView):
    model = Rol
    form_class = Formulario_Rol
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_roles')

def eliminar_Rol(request, pk):
    registro = get_object_or_404(Rol, id=pk)
    registro.delete()
    return redirect('listar_roles')


