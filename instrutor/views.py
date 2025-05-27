from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'aluno/listarAluno.html')

def cadastrar(request):
    return render(request, 'aluno/cadastroAluno.html')
