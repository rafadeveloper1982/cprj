# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleto',
            name='instrucoes',
            field=models.TextField(default='1 - Não receber após 30 dias. \n2 - Multa de 2% após o vencimento. \n3 - Taxa diária de permanência de 0,2%.', verbose_name='Instruções'),
        ),
    ]