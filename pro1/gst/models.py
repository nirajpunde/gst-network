# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver

#Create your models here.
from django.db import models
from django.db.models.signals import pre_save
from .utils import setcost


class businesses(models.Model):
    gst_id = models.AutoField(null=False,primary_key=True)
    acc_no = models.BigIntegerField(null=False,unique=True)
    bus_name = models.CharField(max_length=200,null=False,unique=True)
    email_id = models.EmailField(max_length=200,null=False)
    phone_no = models.BigIntegerField(null=False)
    hq_address = models.CharField(max_length=200,null=False)
    #prod_count = models.IntegerField()
    #turnover = models.PositiveIntegerField(null=False)
    sector = models.CharField(max_length=40,null=False)

    def __str__(self):
        return self.bus_name

class products(models.Model):
    prod_id = models.AutoField(null=False,primary_key=True)
    prod_name = models.CharField(null=False,max_length=20)

    prod_make = models.CharField(null=False,max_length=20)
    prod_type = models.CharField(null=False,max_length=20)

    manuf_price = models.IntegerField(null=False)
    sell_price = models.IntegerField(null=False)

    bus = models.ForeignKey(businesses, on_delete=models.CASCADE,null=True)
    applied_gst = models.IntegerField(null=False)

    def __str__(self):
    	return self.prod_name

class b2b_txn(models.Model):
    b2b_id = models.AutoField(null=False,primary_key=True)
    prod = models.ForeignKey(products, on_delete=models.CASCADE,null=True)

    seller_gst = models.ForeignKey(businesses, on_delete=models.CASCADE,related_name='+',null=True)
    buyer_gst = models.ForeignKey(businesses, on_delete=models.CASCADE,null=True)

    b2b_txn_amt = models.IntegerField()
    b2b_txn_date = models.DateField(auto_now_add=True)

    quantity = models.IntegerField(null=True)
    unit_price = models.IntegerField(null=True)
    total_price= models.IntegerField(null=True)
    total_gst= models.FloatField()

    def __str__(self):
        return str(self.b2b_id)

class b2c_txn(models.Model):
    b2c_id = models.AutoField(null=False,primary_key=True)
    prod_id = models.ForeignKey(products, on_delete=models.CASCADE,null=True)

    seller_gst = models.ForeignKey(businesses, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null=True)
    unit_price =models.IntegerField(null=True)
    total_price =models.IntegerField(null=True)
    b2c_txn_amt = models.IntegerField(null=True)
    total_gst= models.FloatField(null=True)

    b2c_txn_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.b2c_id)


#@receiver(pre_save,sender=b2c_txn)
def set_price(sender,instance,*args,**kwargs):
    obj=products.objects.get(prod_id=instance.prod_id)
    print(obj.sell_price)
    tot_price=obj.sell_price*instance.quantity
    gst_per=obj.applied_gst
    tot_gst=(tot_price*gst_per)/100
    instance.total_gst=tot_gst
    instance.b2c_txn_amt=tot_price+tot_gst

def b2bprice(sender,instance,*args,**kwargs):
    obj=products.objects.get(prod_id=instance.prod_id)
    print(obj.sell_price)
    tot_price=obj.sell_price*instance.quantity
    gst_per=obj.applied_gst
    tot_gst=(tot_price*gst_per)/100
    instance.total_gst=tot_gst
    instance.b2b_txn_amt=tot_price+tot_gst

pre_save.connect(b2bprice,sender=b2b_txn)
pre_save.connect(set_price,sender=b2c_txn)
