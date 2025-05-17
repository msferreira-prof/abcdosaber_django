from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('exibemensagem', views.exibe_mensagem, name="exibir_mensagem"),
]