# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-05 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ninetofiver', '0053_auto_20180301_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperformance',
            name='contract_role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ninetofiver.ContractRole'),
            preserve_default=False,
        ),
    ]
