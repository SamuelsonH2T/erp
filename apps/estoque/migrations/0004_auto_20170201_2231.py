# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20170201_2216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estoque',
            options={'verbose_name': 'Estoque', 'verbose_name_plural': 'Estoque de Produtos'},
        ),
        migrations.AlterField(
            model_name='prateleira',
            name='codigo',
            field=models.CharField(max_length=42),
        ),
        migrations.AlterUniqueTogether(
            name='estoque',
            unique_together=set([('lote', 'prateleira')]),
        ),
    ]
