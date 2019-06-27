from django.urls import path
from .views import *

urlpatterns = [
    path('', get_pagina_login, name ='pagina_login'),
    path('cadastro/', get_pagina_cadastro, name ='pagina_cadastro'),
    path('cadastrar/', cadastrarusuario, name='cadastrar'),
    path('logar/', logarusuario, name='logar')
]