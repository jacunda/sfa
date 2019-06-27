from django.shortcuts import render
from .models import Empresa
from .filtragem_dados.BuscaDados import *
from .filtragem_dados.filtro import *
from django.db.models import Max, Min
from .forms import *
from django.http import HttpResponse


def get_pagina_filtro(request):
    # inserir_Dados_no_Banco()
    dados = get_lista_min_max_dados()
    #print(dados)
    return render(request, 'filtro_template_request.html', {'dados': dados,'setores':setores})


def request_filtros(request):
    if request.method == "POST":
        form = EmpresasRequest(request.POST)
        dados = form.data
        #print(dados)
        dados_filtrados = fitrar_dados(dados)
        return render(request, 'filtro_template_tabela.html', {'dados': dados_filtrados})
