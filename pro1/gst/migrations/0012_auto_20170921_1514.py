# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gst', '0011_b2c_txn_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='b2b_txn',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='b2b_txn',
            name='unit_price',
            field=models.IntegerField(null=True),
        ),
    ]
