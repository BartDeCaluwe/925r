# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-24 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninetofiver', '0064_auto_20180424_0819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performancetype',
            options={'base_manager_name': 'base_objects', 'ordering': ['multiplier']},
        ),
    ]
