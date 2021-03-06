# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-11 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Habitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(blank=True, max_length=300)),
                ('Domicilio', models.CharField(blank=True, max_length=300)),
                ('Ciudad', models.CharField(blank=True, max_length=300)),
                ('Telefono', models.CharField(blank=True, max_length=300)),
                ('Celular', models.CharField(blank=True, max_length=300)),
                ('Email', models.CharField(blank=True, max_length=300)),
                ('Referenciado', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(blank=True, max_length=300)),
                ('Domicilio', models.CharField(blank=True, max_length=300)),
                ('Ciudad', models.CharField(blank=True, max_length=300)),
                ('Telefono', models.CharField(blank=True, max_length=300)),
                ('Celular', models.CharField(blank=True, max_length=300)),
                ('Email', models.CharField(blank=True, max_length=300)),
                ('Referenciado', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagnostico', models.CharField(max_length=300)),
                ('Fecha_ini', models.DateTimeField(blank=True, null=True)),
                ('Frecuencia', models.CharField(max_length=300)),
                ('Apoyo', models.CharField(max_length=300)),
                ('Tipo', models.CharField(max_length=300)),
                ('Porcentaje', models.CharField(max_length=300)),
                ('Sesion', models.CharField(max_length=300)),
                ('Dolor_Fisico', models.CharField(max_length=300)),
                ('Malestar_Emocional', models.CharField(max_length=300)),
                ('Estudio_Medico', models.CharField(max_length=300)),
                ('Firma', models.CharField(max_length=300)),
            ],
        ),
    ]
