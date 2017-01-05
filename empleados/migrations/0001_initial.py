# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('rut', models.IntegerField()),
                ('cargo', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='documento',
            name='dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Empleado'),
        ),
    ]