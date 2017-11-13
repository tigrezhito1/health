# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_pagos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='pagos',
            name='estado',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='tipo',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Tipo'),
        ),
    ]