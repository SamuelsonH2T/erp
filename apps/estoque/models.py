from django.db import models
from utils.models import Cidade



class Fabricante(models.Model):
    nome = models.CharField(max_length=42)
    endereco = models.CharField(max_length=42)
    cnpj = models.CharField(max_length=42, unique=True)
    cidade = models.ForeignKey(Cidade)

    def __str__(self):
        return '{n}'.format(n=self.nome)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'


class Marca(models.Model):
    nome = models.CharField(max_length=42)
    fabricante = models.ForeignKey(Fabricante)

    def __str__(self):
        return '{n}'.format(n=self.nome)

    class Meta:
        unique_together = ('nome', 'fabricante')
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'




class Categoria(models.Model):
    nome = models.CharField(max_length=42, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return '{n}'.format(n=self.nome)


class Produto(models.Model):
    codigo = models.CharField(max_length=42, unique=True)
    nome = models.CharField(max_length=42 )
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)

    def __str__(self):
        return '{n}'.format(n=self.nome)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
