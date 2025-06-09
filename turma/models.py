from django.db import models
from django.utils import timezone

from tiposdeatividade.models import TiposDeAtividade
from aluno.models import Aluno
from instrutor.models import Instrutor

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
                                  help_text='Informe a data final da Turma')
    
    codigo_atividade = models.ForeignKey(TiposDeAtividade, 
                                         null=True, blank=True, on_delete=models.CASCADE,
                                         related_name='atividades')
    
    matricula_monitor = models.ForeignKey(Aluno, null=True, blank=True, 
                                          on_delete=models.SET_NULL,
                                          related_name='alunos')
    
    id_instrutor = models.ForeignKey(Instrutor, null=True, blank=True, on_delete=models.CASCADE,
                                     related_name='instrutores')
    

    def __str__(self):
        return f'{self.numero}'