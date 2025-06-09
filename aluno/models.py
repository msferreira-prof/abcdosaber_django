from django.db import models
from django.utils import timezone

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True,
                                  help_text='Matrícula do Aluno')
    nome = models.CharField(max_length=70,
                            help_text='Informe o nome do Aluno')
    
    data_inicial = models.DateField(null=False,
                                    default=timezone.now(), 
                                    help_text='Informe a data inicial de matrícula do Aluno')

    data_final = models.DateField(null=True,
                                  blank=True,
                                  help_text='Informe a data final de matrícula do Aluno')
    
    def __str__(self):
        return f'{self.matricula} - {self.nome}'