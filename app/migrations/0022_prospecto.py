# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_pagos_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
