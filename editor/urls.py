from django.urls import path #{LIBRERIA URLS DE DJANGO}
from . import views

#{----------------------------------------------------------------------------------------------}

urlpatterns =[  #{LISTA DE URLS CON LOS ARCHIVOS HTML A DESPLEGAR}
    path('crear-tramite', views.crearTipoTramite, name = 'crear_tramite'),
    #path('editar-tramite/<pk>', views.index, name = 'crear_tramite'),
    path('lista-tramites', views.listarTipoDeTramites, name = 'listar_tramites'),
    # URL del modelo Estado
    path('crear-estado', views.crear_Estado, name="crear_estado"),
    path('editar-estado/<pk>', views.editar_Estado.as_view(), name="editar_estado"),
    path('listar-estados', views.listar_Estados, name="listar_estados"),
    # URL del modelo Comentario
    path('crear-comentario', views.crear_Comentario, name="crear_comentario"),
    path('editar-comentario/<pk>', views.editar_Comentario.as_view(), name="editar_comentario"),
    path('listar-comentarios', views.listar_Comentarios, name="listar_comentarios"),
    # URL del modelo Tipo de archivo
    path('crear-tipo-archivo', views.crear_Tipo_Archivo, name="crear_tipo_archivo"),
    path('editar-tipo-archivo/<pk>', views.editar_Tipo_Archivo.as_view(), name="editar_tipo_archivo"),
    path('listar-tipo-archivos', views.listar_Tipo_Archivos, name="listar_tipo_archivos"),

]
#{----------------------------------------------------------------------------------------------}