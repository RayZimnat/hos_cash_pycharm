# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-02 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0031_auto_20160513_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payingauthority',
            name='paying_cut_off_date',
            field=models.CharField(default='Month-end', max_length=50),
        ),
    ]
