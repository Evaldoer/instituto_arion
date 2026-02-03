from django.db import models
from voluntarios.models import Voluntario  # import do outro app

class Praticante(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    voluntario = models.ForeignKey(
        Voluntario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='praticantes'
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ('fila', 'Fila de espera'),
            ('ativo', 'Em atendimento'),
            ('finalizado', 'Finalizado'),
        ],
        default='fila'
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome