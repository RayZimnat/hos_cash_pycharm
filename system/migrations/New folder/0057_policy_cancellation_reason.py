# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-28 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0056_auto_20180228_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='cancellation_reason',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
