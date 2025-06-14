from django.shortcuts import render, redirect

from titulo.models import Titulo
from titulo.forms import TituloForm, TituloAtualizarForm
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

# carregar titulo para atualizar
def carregar_titulo(request, codigo):
    # obter titulo a atualizar basead no codigo informado
    titulo = Titulo.objects.get(pk=codigo)
    contexto = {
        'titulo': titulo,
    }

    return render(request, 'titulo/atualizarTitulo.html', context=contexto)

# atualizar a base de dados para o titulo selecionado
def atualizar(request):
    if request.method == 'POST':
        form = TituloAtualizarForm(request.POST)
        if form.is_valid():

            dados_titulo = form.cleaned_data

            codigo = dados_titulo['codigo']

            titulo = Titulo.objects.get(pk=codigo)
            titulo.descricao = dados_titulo['descricao']

            titulo.save()
        
        # imprimir no console mensagens de erro na validação do formulário
        #else:
        #    print(form.errors)

    return redirect('titulo:listar')
