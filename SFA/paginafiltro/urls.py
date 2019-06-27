from django.urls import path
from .views import *

urlpatterns = [
    path('', get_pagina_filtro, name ='homepage'),
    path('/filtro', request_filtros, name = 'filtro')
]