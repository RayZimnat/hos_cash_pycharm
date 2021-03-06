# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0023_auto_20151111_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='agent_account',
            new_name='agent_phone',
        ),
        migrations.AddField(
            model_name='agent',
            name='agent_branch',
            field=models.CharField(default='Harare', max_length=20),
        ),
        migrations.AddField(
            model_name='policy',
            name='branch',
            field=models.CharField(default='Harare', max_length=20),
        ),
        migrations.AlterField(
            model_name='dependant',
            name='dependant_monthly_premium',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='policy',
            name='payment_method',
            field=models.CharField(choices=[('Ecocash', 'Ecocash'), ('Stop order', 'Stop order'), ('Cash', 'Cash'), ('Netcash', 'Netcash')], default='ecocash', max_length=20),
        ),
    ]
