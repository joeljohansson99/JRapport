# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-25 21:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0027_auto_20190725_2339'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pic',
        ),
    ]