# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-02 08:34
from __future__ import unicode_literals

import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('ninetofiver', '0071_apikey_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhereaboutDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ninetofiver.whereaboutdate_set+', to='contenttypes.ContentType')),
                ('timesheet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ninetofiver.Timesheet')),
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
        migrations.RemoveField(
            model_name='whereabout',
            name='day',
        ),
        migrations.RemoveField(
            model_name='whereabout',
            name='timesheet',
        ),
        migrations.AddField(
            model_name='whereabout',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='whereabout',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='whereabout',
            name='location',
            field=models.CharField(choices=[('home', 'Home'), ('office', 'Office'), ('out_of_office', 'Out of office'), ('other', 'Other')], max_length=32),
        ),
        migrations.AddField(
            model_name='whereaboutdate',
            name='whereabout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ninetofiver.Whereabout'),
        ),
    ]
