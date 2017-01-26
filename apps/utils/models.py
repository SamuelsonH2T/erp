from django.db import models


class Regiao(models.Model):
    nome = models.CharField(max_length=42, unique=True)
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return "{n}({s})".format(n=self.nome, s=self.sigla)

    class Meta:
        verbose_name = 'Regiao'
        verbose_name_plural = 'Regiões'



class Estado(models.Model):
    nome = models.CharField(max_length=42, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    regiao = models.ForeignKey(Regiao)

    def __str__(self):
        return "{n}".format(n=self.nome)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(models.Model):
    nome = models.CharField(max_length=42,unique=True)
    estado = models.ForeignKey(Estado)
    ddd = models.CharField(max_length=2)

    def __str__(self):
        return "{n}".format(n=self.nome)


    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
