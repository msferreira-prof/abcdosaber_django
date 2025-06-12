from django.shortcuts import render, redirect

from titulo.models import Titulo
from titulo.forms import TituloForm
from instrutor.models import Instrutor


# Create your views here.
def listar(request):

    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }

    return render(request, 'titulo/listarTitulos.html', context=contexto)


# carregar a pagina para cadastrar um titulo na base de dados
def cadastro(request):
    return render(request, 'titulo/cadastroTitulos.html')


# acao de cadastrar um titulo na base de dados
def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao = dados_titulo['descricao']
        )
        titulo.save()

    return render(request, 'titulo/cadastroTitulos.html')


# excluir um titulo
def excluir(request, codigo):
    titulo = Titulo.objects.get(pk=codigo)

    # verifica se ha um instrutor relacionado ao tiutlo a excluir
    # caso contrario, o titulo poderá ser excluido
    instrutores = Instrutor.objects.filter(codigo_titulo=codigo)
    if not instrutores:
        titulo.delete()

    return redirect('titulo:listar')



