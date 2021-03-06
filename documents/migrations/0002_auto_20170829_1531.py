# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 15:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='documents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='images', to=settings.AUTH_USER_MODEL),
        ),
    ]
