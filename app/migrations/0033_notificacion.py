# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-13 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20171111_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('fecha', models.CharField(max_length=300)),
                ('user', models.CharField(max_length=300)),
            ],
        ),
    ]
