# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-03 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0032_auto_20160602_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agent_email',
            field=models.EmailField(blank=True, max_length=75),
        ),
    ]
