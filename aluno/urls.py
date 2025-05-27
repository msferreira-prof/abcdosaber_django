from django.urls import path
from . import views 

app_name = 'aluno'

urlpatterns = [
    path('lista', views.listar, name='listar'),
    path('cadastro', views.cadastrar, name='cadastrar'),
]