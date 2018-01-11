# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-11 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180110_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='layerinfo',
            name='max_zoom',
            field=models.PositiveIntegerField(blank=True, default=30, null=True),
        ),
        migrations.AddField(
            model_name='layerinfo',
            name='min_zoom',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
