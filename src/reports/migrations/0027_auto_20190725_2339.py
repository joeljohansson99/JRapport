# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-25 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0026_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='photo',
            field=models.FileField(upload_to='files'),
        ),
    ]
