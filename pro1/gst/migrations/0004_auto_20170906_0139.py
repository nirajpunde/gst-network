# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gst', '0003_txn_txn_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='txn',
            name='txn_amt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='txn',
            name='txn_no',
            field=models.IntegerField(null=True),
        ),
    ]
