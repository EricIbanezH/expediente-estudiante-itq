from django.urls import path #{LIBRERIA URLS DE DJANGO}
from . import views

#{----------------------------------------------------------------------------------------------}

urlpatterns =[  #{LISTA DE URLS CON LOS ARCHIVOS HTML A DESPLEGAR}
    path('crear-tramite', views.crearTipoTramite, name = 'crear_tramite'),
    #path('editar-tramite/<pk>', views.index, name = 'crear_tramite'),
    path('lista-tramites', views.listarTipoDeTramites, name = 'listar_tramites'),
    
    path('crear-estado', views.crear_Estado, name="crear_estado"),
    #path('crear-estado/<pk>', views.index, name="crear_estado"),
    path('listar-estados', views.listar_Estados, name="listar_estados"),

]
#{----------------------------------------------------------------------------------------------}