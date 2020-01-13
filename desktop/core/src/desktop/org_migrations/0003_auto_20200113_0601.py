# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-13 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0001_initial'),
        ('desktop', '0002_auto_20200112_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('dialect', models.CharField(db_index=True, help_text='Type of connector, e.g. hive, mysql... ', max_length=32)),
                ('settings', models.TextField(default='{}')),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Time last modified')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmin.Organization')),
            ],
            options={
                'verbose_name': 'connector',
                'verbose_name_plural': 'connectors',
            },
        ),
        migrations.AlterUniqueTogether(
            name='connector',
            unique_together=set([('name', 'organization')]),
        ),
    ]
