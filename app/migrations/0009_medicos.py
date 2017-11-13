# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-16 20:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_auto_20171016_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(blank=True, max_length=300)),
                ('Domicilio', models.CharField(max_length=300)),
                ('Ciudad', models.CharField(blank=True, max_length=300)),
                ('Telefono', models.CharField(blank=True, max_length=300)),
                ('Celular', models.CharField(blank=True, max_length=300)),
                ('Email', models.CharField(max_length=300)),
                ('Referenciado', models.CharField(blank=True, max_length=300)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]