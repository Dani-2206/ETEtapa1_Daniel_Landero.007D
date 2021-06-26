from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('creacion_p',form_creacion,name='creacion_usuario'),
    path('mostrar_p',mostrar,name='mostrar'),
    path('modificar/<id>', modificar ,name='modificar'),
    path('eliminar/<id>',eliminar,name='eliminar')
]