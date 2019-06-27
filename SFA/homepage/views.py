from django.shortcuts import render 
from django.http import HttpResponse
from .forms import CadastrarNovoUsuario, Logar
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def get_pagina_login(request):
    return render(request, 'home_template_login.html', {})


def get_pagina_cadastro(request):
    return render(request, 'home_template_cadastro.html', {})

def logarusuario(request):
    if request.method == "POST":
        form = Logar(request.POST)
        if form.is_valid():
            dados = form.data
            user = authenticate(username=dados['usuario'], password=dados['senha'])
            if user is not None:
                login(request, user)
                return HttpResponse('O novo usuario esta logado no sistema .')
            else:
                form.adiciona_erro(message='Usuario ou senha esta errado')
                return render(request, 'home_template_login.html', {'form': form})
        else:
            return render(request, 'filtro_template_buscas.html')


def cadastrarusuario(request):
    if request.method == "POST":
        form = CadastrarNovoUsuario(request.POST)
        if form.is_valid():
            dados = form.data
            print(dados['usuario'])
            novo_user = User.objects.create_user(dados['usuario'], dados['email'], dados['senha'])
            novo_usuario = Usuario(nome=dados['nome'], user=novo_user)
            novo_usuario.save()
            return HttpResponse('O cadastro foi feito !')
        else:
            return render(request, 'home_template_login.html', {'form': form})
