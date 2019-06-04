# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-25 12:03
from __future__ import unicode_literals

import datetime
import dirtyfields.dirtyfields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('ninetofiver', '0084_auto_20181008_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('period_starts_at', models.DateField(default=datetime.date.today)),
                ('period_ends_at', models.DateField(default=datetime.date.today)),
                ('date', models.DateField(default=datetime.date.today)),
                ('reference', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ninetofiver.Contract')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ninetofiver.invoice_set+', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
                'base_manager_name': 'base_objects',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('amount', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, validators=[django.core.validators.MinValueValidator(-9999999), django.core.validators.MaxValueValidator(9999999)])),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ninetofiver.Invoice')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ninetofiver.invoiceitem_set+', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
                'base_manager_name': 'base_objects',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
