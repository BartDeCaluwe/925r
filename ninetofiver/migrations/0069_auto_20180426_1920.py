# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-26 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninetofiver', '0068_apikey_read_only'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='read_only',
            field=models.BooleanField(default=True),
        ),
    ]
