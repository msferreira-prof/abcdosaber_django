from django.urls import path
from . import views 

app_name = 'utilitarios'

urlpatterns = [
    path('contato', views.carregar_contato, name="contato"),
]