# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_auto_20180902_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverinfo',
            name='server_type',
            field=models.CharField(choices=[('physical', 'physical'), ('virtual', 'virtual')], default='physical', max_length=10),
        ),
    ]
