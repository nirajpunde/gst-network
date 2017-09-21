# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gst', '0005_auto_20170906_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='b2b_txn',
            fields=[
                ('b2b_id', models.AutoField(primary_key=True, serialize=False)),
                ('b2b_txn_amt', models.IntegerField()),
                ('b2b_txn_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='b2c_txn',
            fields=[
                ('b2c_id', models.AutoField(primary_key=True, serialize=False)),
                ('b2c_txn_amt', models.IntegerField()),
                ('b2c_txn_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='businesses',
            fields=[
                ('gst_id', models.AutoField(primary_key=True, serialize=False)),
                ('acc_no', models.BigIntegerField(unique=True)),
                ('bus_name', models.CharField(max_length=200, unique=True)),
                ('email_id', models.EmailField(max_length=200)),
                ('phone_no', models.BigIntegerField()),
                ('hq_address', models.CharField(max_length=200)),
                ('prod_count', models.IntegerField()),
                ('turnover', models.PositiveIntegerField()),
                ('sector', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=20)),
                ('hsn', models.BigIntegerField(default=0, unique=True)),
                ('prod_make', models.CharField(max_length=20)),
                ('prod_type', models.CharField(max_length=20)),
                ('manuf_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('applied_gst', models.IntegerField()),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gst.businesses')),
            ],
        ),
        migrations.DeleteModel(
            name='txn',
        ),
        migrations.AddField(
            model_name='b2c_txn',
            name='prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gst.products'),
        ),
        migrations.AddField(
            model_name='b2c_txn',
            name='seller_gst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gst.businesses'),
        ),
        migrations.AddField(
            model_name='b2b_txn',
            name='buyer_gst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gst.businesses'),
        ),
        migrations.AddField(
            model_name='b2b_txn',
            name='prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gst.products'),
        ),
        migrations.AddField(
            model_name='b2b_txn',
            name='seller_gst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gst.businesses'),
        ),
    ]
