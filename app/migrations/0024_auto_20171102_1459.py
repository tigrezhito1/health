# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-02 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20171030_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atencion',
            name='citas',
        ),
        migrations.AddField(
            model_name='atencion',
            name='medicos',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Medicos'),
        ),
    ]
