from django.db import models


class Regiao(models.Model):
    nome = models.CharField(max_length=42, unique=True)
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return "{n}({s})".format(n=self.nome, s=self.sigla)

    class Meta:
        verbose_name = 'Regiao'
        verbose_name_plural = 'Regiões'
