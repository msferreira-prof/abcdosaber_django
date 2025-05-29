from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'titulo/listarTitulos.html')

def cadastrar(request):
    return render(request, 'titulo/cadastroTitulos.html')
