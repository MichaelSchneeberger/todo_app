# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='havetotask',
            name='due_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='havetotask',
            name='should_be_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='havetotask',
            name='start_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
