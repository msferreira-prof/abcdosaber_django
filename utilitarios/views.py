from django.shortcuts import render

# Create your views here.
def carregar_contato(request):
    return render(request, 'utilitarios/contato.html')