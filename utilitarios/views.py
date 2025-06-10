from django.shortcuts import render, redirect

from utilitarios import utils

# Create your views here.
def carregar_contato(request):
    return render(request, 'utilitarios/contato.html')

def popular_bd(request):
    utils.truncar_tabelas()
    utils.popular_tiposdeatividade()
    utils.popular_titulo()
    utils.popular_aluno()
    #utils.popular_instrutor()
    utils.popular_turma()

    return redirect('/')

