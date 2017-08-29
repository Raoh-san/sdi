# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170825_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layerinfo',
            name='metadata_id',
        ),
        migrations.AddField(
            model_name='layerinfo',
            name='metadata',
            field=models.ForeignKey(default='fcae40d9-e6a8-4401-ab1d-fa2743a6aaa5', on_delete=django.db.models.deletion.PROTECT, related_name='layer_info_md', to='api.MetaData'),
            preserve_default=False,
        ),
    ]
