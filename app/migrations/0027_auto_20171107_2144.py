# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-07 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20171107_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='area',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Area'),
        ),
    ]
