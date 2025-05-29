from django.shortcuts import HttpResponse, render

# Create your views here.
def listar(request):
    return render(request, 'tiposdeatividade/listarTiposAtividade.html')

def cadastrar(request):
    return render(request, 'tiposdeatividade/cadastroTiposAtividade.html')
