# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_metadata_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='geometry_type',
            field=models.CharField(choices=[('Point', 'Point'), ('LineString', 'LineString'), ('Polygon', 'Polygon'), ('MultiPoint', 'MultiPoint'), ('MultiLineString', 'MultiLineString'), ('MultiPolygon', 'MultiPolygon')], default='Point', max_length=16),
            preserve_default=False,
        ),
    ]
