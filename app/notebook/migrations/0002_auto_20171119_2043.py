# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
