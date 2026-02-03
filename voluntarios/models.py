from django.db import models

class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    area = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.area})"