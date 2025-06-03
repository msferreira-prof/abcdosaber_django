from django.urls import path
from . import views 

app_name = 'turma'

urlpatterns = [
    path('cadastro', views.cadastrar, name='cadastrar'),
    path('lista', views.listar, name='listar'),
    path('registrar_ausencia', views.registrar_ausencia, name='registrar_ausencia'),
]