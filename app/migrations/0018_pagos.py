# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20171027_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('monto', models.CharField(blank=True, max_length=300)),
                ('estado', models.CharField(blank=True, max_length=300)),
                ('tipo', models.CharField(blank=True, max_length=300)),
                ('cita', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Citas')),
                ('pacientes', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Pacientes')),
            ],
        ),
    ]
