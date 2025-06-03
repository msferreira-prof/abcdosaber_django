from django.db import models
from django.utils import timezone

# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(primary_key=True,
                                  help_text='Matrícula do Aluno')
    horario_aula = models.TimeField(help_text='Informe a hora de início da Turma')
    
    duracao_aula = models.SmallIntegerField(help_text='Informe a duração em horas da Turma')

    data_inicial = models.DateField(null=False,
                                    default=timezone.now(), 
                                    help_text='Informe a data inicial da Turma')

    data_final = models.DateField(null=True,
                                  blank=True,
                                  default=timezone.now(), 
                                  help_text='Informe a data final da Turma')
    
    def __str__(self):
        return f'{self.numero}'