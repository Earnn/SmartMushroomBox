# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxapp', '0009_auto_20170727_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]