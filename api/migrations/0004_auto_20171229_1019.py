# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-29 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_usermap_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayerGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='layergroup_name', to='api.MessageRecord')),
            ],
        ),
        migrations.AddField(
            model_name='layerinfo',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.LayerGroup'),
        ),
    ]
