from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    t_html = '<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Escola</title></head><body><p>Esta é a página inicial do App Utilitários</p></body></html>'
    return HttpResponse(t_html)
