# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-16 00:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171015_0421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citas',
            old_name='direccion',
            new_name='descripcion',
        ),
    ]
