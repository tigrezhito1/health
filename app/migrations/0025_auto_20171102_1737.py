# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-02 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20171102_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='endhora',
            field=models.TimeField(blank=True, null=True, verbose_name='Inicio'),
        ),
        migrations.AddField(
            model_name='citas',
            name='starthora',
            field=models.TimeField(blank=True, null=True, verbose_name='Inicio'),
        ),
    ]