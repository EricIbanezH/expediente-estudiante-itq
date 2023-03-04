from email.policy import default
from django.shortcuts import render
from editor.formularios import FormularioTramite
from editor.models import Tipo_Tramite, Rel_Tram_Rol,Rol,Rel_Tram_Doc,Tipo_Documento, Tramite

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
