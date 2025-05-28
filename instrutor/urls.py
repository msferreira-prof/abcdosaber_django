from django.urls import path
from . import views 

app_name = 'instrutor'

urlpatterns = [
    path('cadastro', views.cadastrar, name='cadastrar'),
    path('lista', views.listar, name='listar'),
]