from django.db import models
from django.utils import timezone

from titulo.models import Titulo

# Create your models here.
class Instrutor(models.Model):
    id = models.AutoField(primary_key=True,
                                  help_text='Matrícula do Instrutor')
    
    rg = models.CharField(max_length=15,
                          help_text='Informe o RG do Instrutor')

    nome = models.CharField(max_length=70,
                            help_text='Informe o nome do Instrutor')
    
    data_nascimento = models.DateField(null=True,
                                       blank=True,
                                       default=timezone.now(), 
                                       help_text='Informe a data de nascimento do Instrutor')

    telefone = models.CharField(max_length=9,
                                help_text='Informe o telefone do Instrutor')
    
    ddd = models.CharField(max_length=3,
                           help_text='Informe o DDD do telefone do Instrutor')

    codigo_titulo = models.ForeignKey(Titulo, 
                                      null=True,
                                      blank=True,
                                      related_name='titulos', 
                                      on_delete=models.SET_NULL,
                                      db_column='titulo_codigo')

    def __str__(self):
        return f'{self.id} - {self.nome}'