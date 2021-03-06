# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleto', '0007_auto_20171217_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='carteira_remessa',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='conta',
            name='cedente_seguencia_arquivo',
            field=models.IntegerField(null=True, verbose_name='Sequencia Arquivo'),
        ),
        migrations.AddField(
            model_name='conta',
            name='digito_agencia_cedente',
            field=models.CharField(max_length=1, null=True, verbose_name='Dígito da Agência do Cedente'),
        ),
        migrations.AddField(
            model_name='conta',
            name='digito_conta_cedente',
            field=models.CharField(max_length=1, null=True, verbose_name='Dígito da Conta do Cedente'),
        ),
        migrations.AlterField(
            model_name='conta',
            name='conta_cedente',
            field=models.CharField(max_length=9, verbose_name='Conta Cedente'),
        ),
        migrations.AlterField(
            model_name='conta',
            name='especie_documento',
            field=models.IntegerField(blank=True, verbose_name='Espécie do Documento'),
        ),
    ]
