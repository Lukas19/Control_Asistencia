# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0008_auto_20170112_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
