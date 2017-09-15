# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from gst.models import txn
from django.views.generic import ListView
import MySQLdb


# Create your views here.
def home(request):
    context= {}
    return render(request,"GST.html",context)


def show_txn(request):
    qs = txn.objects.raw("select * from gst_txn")
    context = {
    "obj_list": qs,
    }
    return render(request,"base.html",context)


# def show_txn(request):
#     qs = txn.objects.all()
#     context = {
#     "obj_list": qs,
#     }
#     return render(request,"base.html",context)
