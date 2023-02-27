from django.urls import path #{LIBRERIA URLS DE DJANGO}
from . import views

#{----------------------------------------------------------------------------------------------}

urlpatterns =[  #{LISTA DE URLS CON LOS ARCHIVOS HTML A DESPLEGAR}
    path('', views.index, name='index'),

]
#{----------------------------------------------------------------------------------------------}