from django.urls import path #{LIBRERIA URLS DE DJANGO}
from . import views
from editor import views as viewsEditor

#{----------------------------------------------------------------------------------------------}

urlpatterns =[  #{LISTA DE URLS CON LOS ARCHIVOS HTML A DESPLEGAR}
    path('', views.index, name='index'),
    path('crear-tramite', viewsEditor.crearTipoTramite, name='crear-tramite'),
    path('lista-tramites',viewsEditor.listarTipoDeTramites,name='lista-tramites'),

]
#{----------------------------------------------------------------------------------------------}