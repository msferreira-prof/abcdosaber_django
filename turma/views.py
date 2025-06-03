from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request, 'turma/cadastroTurma.html')

def listar(request):
    return render(request, 'turma/listarTurmas.html')

def registrar_ausencia(request):
    return render(request, 'turma/registroAusencia.html')

