# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_auto_20170110_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(upload_to='/Upload'),
        ),
    ]
