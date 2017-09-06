# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Create your models here.
class txn(models.Model):
    txn_no= models.IntegerField(null=True)

    txn_det= models.CharField(max_length=20)
    txn_date= models.DateField(auto_now_add=True)
    txn_amt= models.IntegerField(null=True)

    def __str__(self):
        return str(self.txn_no)
