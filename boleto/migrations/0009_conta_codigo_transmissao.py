# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleto', '0008_auto_20171221_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='codigo_transmissao',
            field=models.CharField(max_length=15, null=True, verbose_name='Código de Transmissão'),
        ),
    ]
