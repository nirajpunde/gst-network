# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gst', '0008_auto_20170916_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='hsn',
        ),
    ]
