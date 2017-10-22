# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import businesses
from .models import products
from .models import b2b_txn
from .models import b2c_txn
from django.views.generic import ListView
import MySQLdb
from .forms import Businessform,Update_business_form,Upconbusform,Delete_business_form,Productform,delete_b2c_form,update_b2b_form
from .forms import Update_product_form,product_update_conf,delete_product_form,b2c_txn_create,update_b2c_form,b2b_txn_create,delete_b2b_form
from django.http import HttpResponseRedirect
#from dal import autocomplete
from django.shortcuts import redirect



# Create your views here.
"""class GST_idAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor

        qs = businesses.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs"""

def home(request):
     context= {}
     return render(request,"GST.html",context)

def product(request):
    context={}
    return render(request,"product.html",context)

def business(request):
    context={}
    return render(request,"business.html",context)

def b2b(request):
    context={}
    return render(request,"b2b.html",context)

def b2c(request):
    context={}
    return render(request,"b2c.html",context)

def display(request):
    qs = businesses.objects.raw("select * from gst_businesses")
    context = {
    "obj_list": qs,
    }
    return render(request,"base.html",context)


def create_business(request):
    form = Businessform(request.POST)
    if request.method == "POST":
        acc_no     =   int(request.POST.get('acc_no'))
        bus_name   =   str(request.POST.get('bus_name'))
        email_id   =   str(request.POST.get('email_id'))
        phone_no   =   int(request.POST.get('phone_no'))
        hq_address =   str(request.POST.get('hq_address'))
        sector     =   str(request.POST.get('sector'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="insert into gst_businesses(acc_no,bus_name,email_id,phone_no,hq_address,sector) values(%d,'%s','%s',%d,'%s','%s')"%(acc_no,bus_name,email_id,phone_no,hq_address,sector)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/business/")
    heading="Insert Your Business Details"
    context={
        'form':form,
        'heading':heading,
    }

    return render(request,"businessform.html",context)

def update_business(request):
    form = Update_business_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('gst_id'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_businesses where gst_id = %d"%(temp)
        print(query)
        qs = businesses.objects.get(pk=temp)
        print(qs.gst_id)
        print(qs)
        if qs:
            link="http://127.0.0.1:8000/business/update/confirm/%d"%(qs.gst_id)
            return redirect(link)
        else:
            return HttpResponseRedirect("/business/errors")
    heading="Enter GST ID of the Business you want to Update"
    context={
    'form':form,
    'heading':heading,
    }
    return render(request,"busupdateform.html",context)


def update_confirm(request,*args,**kwargs):
    gst_id = int(kwargs.get('id'))
    print("inside update conform")
    print(gst_id)

    query="select * from gst_businesses where gst_id = %d"%(gst_id)
    qs = businesses.objects.get(pk=gst_id)
    print(qs)

    form = Update_business_form(request.POST)
    if request.method == "POST":
        acc_no     =   int(request.POST.get('acc_no'))
        bus_name   =   str(request.POST.get('bus_name'))
        email_id   =   str(request.POST.get('email_id'))
        phone_no   =   int(request.POST.get('phone_no'))
        hq_address =   str(request.POST.get('hq_address'))
        sector     =   str(request.POST.get('sector'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="update gst_businesses set acc_no=%d,bus_name='%s',email_id='%s',phone_no=%i,hq_address='%s',sector='%s' where gst_id=%d"%(acc_no,bus_name,email_id,phone_no,hq_address,sector,gst_id)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/business/")

    context={
        'form':form,
        'qs'  :qs,
    }

    return render(request,"busupconform.html",context)

def delete_business(request):
    form = Delete_business_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('gst_id'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_businesses where gst_id = %d"%(temp)
        print(query)
        qs = businesses.objects.get(pk=temp)
        print(qs.gst_id)
        print(qs)
        if qs:
            link="http://127.0.0.1:8000/business/delete/confirm/%d"%(qs.gst_id)
            return redirect(link)
        else:
            return HttpResponseRedirect("/business/errors")
    heading="Select GST ID of the Business you wish to Delete"
    context={'form':form,'heading':heading}
    return render(request,"busdeleteform.html",context)

def delete_confirm_bus(request,*args,**kwargs):
    gst_id = int(kwargs.get('id'))
    print("inside update conform")
    print(gst_id)

    query="select * from gst_businesses where gst_id = %d"%(gst_id)
    qs = businesses.objects.get(pk=gst_id)
    print(qs)


    if request.method == "POST":

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="delete from gst_businesses where gst_id=%d"%(gst_id)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/business/")

    context={
        'qs'  :qs,
    }

    return render(request,"busdelconform.html",context)

def create_product(request):
    form = Productform(request.POST)
    if request.method == "POST":
        prod_name     =   str(request.POST.get('prod_name'))
        prod_make     =   str(request.POST.get('prod_make'))
        prod_type     =   str(request.POST.get('prod_type'))
        manuf_price   =   int(request.POST.get('manuf_price'))
        sell_price    =   int(request.POST.get('sell_price'))
        manufacturer  =   str(request.POST.get('manufacturer'))
        applied_gst   =   int(request.POST.get('applied_gst'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="insert into gst_products (prod_name,prod_make,prod_type,manuf_price,sell_price,bus_id,applied_gst) values('%s','%s','%s',%d,%d,'%s',%d)"%(prod_name,prod_make,prod_type,manuf_price,sell_price,manufacturer,applied_gst)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/product/")
    heading ="Insert Product Details"
    context={
        'form':form,
        'heading':heading,
    }

    return render(request,"productform.html",context)

def productdisplay(request):
    qs=products.objects.raw("select * from gst_products")
    context={
    "obj_list":qs,
    }
    return render(request,"productdisplay.html",context)

def update_product(request):
    form = Update_product_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('prod_id'))
        print("this is temp")
        print(temp)
        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_products where prod_id = %d"%(temp)

        qs = products.objects.get(pk=temp)

        if qs:
            link="http://127.0.0.1:8000/product/update/confirm/%d"%(qs.prod_id)
            return redirect(link)
        else:
            return HttpResponseRedirect("/product/errors")
    heading="Enter GST ID of Product you want to Update"
    context={'form':form,'heading':heading}
    return render(request,"busupdateform.html",context)

def product_update_confirm(request,*args,**kwargs):
    prod_id = int(kwargs.get('id'))
    print("inside update conform")
    print(prod_id)

    query="select * from gst_products where prod_id = %d"%(prod_id)
    qs = products.objects.get(pk=prod_id)
    print(qs.prod_id)

    form = Update_business_form(request.POST)
    if request.method == "POST":
        prod_name     =   str(request.POST.get('prod_name'))
        prod_make     =   str(request.POST.get('prod_make'))
        prod_type     =   str(request.POST.get('prod_type'))
        manuf_price   =   int(request.POST.get('manuf_price'))
        sell_price    =   int(request.POST.get('sell_price'))
        manufacturer  =   int(request.POST.get('bus_id'))
        applied_gst   =   int(request.POST.get('applied_gst'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="update gst_products set prod_name='%s',prod_make='%s',prod_type='%s',manuf_price=%d,sell_price=%d, bus_id=%d,applied_gst=%d where prod_id=%d"%(prod_name,prod_make,prod_type,manuf_price,sell_price,manufacturer,applied_gst,prod_id)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/product/")
    context={
        'form':form,
        'qs'  :qs,
    }

    return render(request,"product_update_confirm.html",context)

def delete_product(request):
    form = delete_product_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('prod_id'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_products where prod_id = %d"%(temp)
        print(query)
        qs = products.objects.get(pk=temp)
        print(qs.prod_id)
        print(qs)
        if qs:
            link="http://127.0.0.1:8000/product/delete/confirm/%d"%(qs.prod_id)
            return redirect(link)
        else:
            return HttpResponseRedirect("/business/errors")

    context={'form':form}
    return render(request,"busdeleteform.html",context)

def delete_confirm(request,*args,**kwargs):
    prod_id = int(kwargs.get('id'))
    print("inside update conform")
    print(prod_id)

    query="select * from gst_businesses where prod_id = %d"%(prod_id)
    qs = products.objects.get(pk=prod_id)
    print(qs)


    if request.method == "POST":

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="delete from gst_products where prod_id=%d"%(prod_id)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/product/")
    context={
        'qs'  :qs,
    }

    return render(request,"prod_del_con.html",context)

def add_b2c_txn(request):
    form = b2c_txn_create(request.POST)
    if request.method == "POST":
        prod_id = int(request.POST.get('prod_id'))
        seller_gst = int(request.POST.get('seller_gst'))
        quantity = int(request.POST.get('quantity'))
        q="select * from gst_products where prod_id=%d"%(prod_id)
        print(q)
        prod = products.objects.raw(q)[0]

        unit_price=prod.sell_price
        gst_per=prod.applied_gst
        total_cost=quantity*unit_price
        total_gst=total_cost*gst_per/100
        txn_amt=total_cost+total_gst

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="insert into gst_b2c_txn (prod_id_id,seller_gst_id,quantity,unit_price,total_price,b2c_txn_amt,total_gst,b2c_txn_date) values(%d,%d,%d,%d,%d,%d,%d,now())"%(prod_id,seller_gst,quantity,unit_price,total_cost,txn_amt,total_gst)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/b2c/")
    context={
        'form':form
    }

    return render(request,"businessform.html",context)

def display_b2c(request):
    qs=b2c_txn.objects.raw("select * from gst_b2c_txn")
    context={
    'obj_list':qs
    }
    return render(request,"display_b2c.html",context)

def update_b2c(request):
    form = update_b2c_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('b2c_id'))
        print("this is temp")
        print(temp)
        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_b2c_txn where b2c_id = %d"%(temp)
        print(query)
        qs = b2c_txn.objects.raw(query)[0]

        if qs:
            link="http://127.0.0.1:8000/b2c/update/confirm/%d"%(qs.b2c_id)
            return redirect(link)
        else:
            return HttpResponseRedirect("/product/errors")

    heading ="Enter B2C Transaction ID"
    context={
        'form':form,
        'heading':heading,
    }
    return render(request,"busupdateform.html",context)

def b2c_update_confirm(request,*args,**kwargs):
    b2c_id = int(kwargs.get('id'))
    print("inside update conform")


    query="select * from gst_b2c_txn where b2c_id = %d"%(b2c_id)
    qs = b2c_txn.objects.raw(query)[0]


    form = b2c_txn_create(request.POST)
    if request.method == "POST":
        prod_id = int(request.POST.get('prod_id'))
        seller_gst = int(request.POST.get('seller_gst'))
        quantity = int(request.POST.get('quantity'))
        q="select * from gst_products where prod_id=%d"%(prod_id)
        print(q)
        prod = products.objects.raw(q)[0]

        unit_price=prod.sell_price
        gst_per=prod.applied_gst
        total_cost=quantity*unit_price
        total_gst=total_cost*gst_per/100
        txn_amt=total_cost+total_gst

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="update gst_b2c_txn set prod_id_id=%d,seller_gst_id=%d,quantity=%d,unit_price=%d,total_price=%d,total_gst=%d,b2c_txn_amt=%d where b2c_id=%d"%(prod_id,seller_gst,quantity,unit_price,total_cost,total_gst,txn_amt,b2c_id)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/b2c/")
    context={
        'form':form,
        'qs'  :qs,
    }

    return render(request,"busupdateform.html",context)

def delete_b2c(request):
    form = delete_b2c_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('b2c_id'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_b2c_txn where b2c_id = %d"%(temp)
        print(query)
        qs = b2c_txn.objects.raw(query)[0]

        if qs:
            link="http://127.0.0.1:8000/b2c/delete/confirm/%d"%(qs.b2c_id)
            return redirect(link)
        else:
            return HttpResponseRedirect("/b2c/errors")

    heading ="Enter B2C Transaction ID"
    context={
        'form':form,
        'heading':heading,
    }
    return render(request,"busdeleteform.html",context)

def b2c_delete_confirm(request,*args,**kwargs):
    b2c_id = int(kwargs.get('id'))
    print("inside delete conform")

    query="select * from gst_b2c_txn where b2c_id = %d"%(b2c_id)
    qs = b2c_txn.objects.raw(query)[0]
    if request.method == "POST":

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="delete from gst_b2c_txn where b2c_id=%d"%(b2c_id)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/b2c/")
    context={
        'qs'  :qs,
    }

    return render(request,"b2c_del_con.html",context)

def add_b2b_txn(request):
    form = b2b_txn_create(request.POST)
    if request.method == "POST":
        prod_id = int(request.POST.get('prod_id'))
        seller_gst = int(request.POST.get('seller_gst'))
        buyer_gst  = int(request.POST.get('buyer_gst'))
        quantity = int(request.POST.get('quantity'))
        q="select * from gst_products where prod_id=%d"%(prod_id)
        print(q)
        prod = products.objects.raw(q)[0]

        unit_price=prod.sell_price
        gst_per=prod.applied_gst
        total_cost=quantity*unit_price
        total_gst=total_cost*gst_per/100
        txn_amt=total_cost+total_gst

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="insert into gst_b2b_txn (prod_id,seller_gst_id,buyer_gst_id,quantity,unit_price,total_price,b2b_txn_amt,total_gst,b2b_txn_date) values(%d,%d,%d,%d,%d,%d,%d,%d,now())"%(prod_id,seller_gst,buyer_gst,quantity,unit_price,total_cost,txn_amt,total_gst)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/b2b/")
    context={
        'form':form
    }

    return render(request,"businessform.html",context)

def display_b2b(request):
    qs=b2b_txn.objects.raw("select * from gst_b2b_txn")
    context={
    'obj_list':qs
    }
    return render(request,"display_b2b.html",context)

def update_b2b(request):
    form = update_b2b_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('b2b_id'))
        print("this is temp")
        print(temp)
        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_b2b_txn where b2b_id = %d"%(temp)
        print(query)
        qs = b2b_txn.objects.raw(query)[0]

        if qs:
            link="http://127.0.0.1:8000/b2b/update/confirm/%d"%(qs.b2b_id)
            return redirect(link)
        else:
            return HttpResponseRedirect("/product/errors")

    heading ="Update B2B Transaction Details"
    context={
        'form':form,
        'heading':heading,
    }
    return render(request,"busupdateform.html",context)

def b2b_update_confirm(request,*args,**kwargs):
    b2b_id = int(kwargs.get('id'))
    print("inside update conform")


    query="select * from gst_b2b_txn where b2b_id = %d"%(b2b_id)
    qs = b2b_txn.objects.raw(query)[0]


    form = b2b_txn_create(request.POST)
    if request.method == "POST":
        prod_id = int(request.POST.get('prod_id'))
        seller_gst = int(request.POST.get('seller_gst'))
        buyer_gst = int(request.POST.get('buyer_gst'))
        quantity = int(request.POST.get('quantity'))
        q="select * from gst_products where prod_id=%d"%(prod_id)
        print(q)
        prod = products.objects.raw(q)[0]

        unit_price=prod.sell_price
        gst_per=prod.applied_gst
        total_cost=quantity*unit_price
        total_gst=total_cost*gst_per/100
        txn_amt=total_cost+total_gst

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="update gst_b2b_txn set prod_id=%d,seller_gst_id=%d,buyer_gst_id=%d,quantity=%d,unit_price=%d,total_price=%d,total_gst=%d,b2b_txn_amt=%d where b2b_id=%d"%(prod_id,seller_gst,buyer_gst,quantity,unit_price,total_cost,total_gst,txn_amt,b2b_id)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/b2b/")
    context={
        'form':form,
        'qs'  :qs,
    }

    return render(request,"busupdateform.html",context)


def delete_b2b(request):
    form = delete_b2b_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('b2b_id'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_b2b_txn where b2b_id = %d"%(temp)
        print(query)
        qs = b2b_txn.objects.raw(query)[0]

        if qs:
            link="http://127.0.0.1:8000/b2b/delete/confirm/%d"%(qs.b2b_id)
            return redirect(link)
        else:
            return HttpResponseRedirect("/b2b/errors")

    heading ="Enter B2B Transaction ID"
    context={
        'form':form,
        'heading':heading,
    }

    return render(request,"busdeleteform.html",context)

def b2b_delete_confirm(request,*args,**kwargs):
    b2b_id = int(kwargs.get('id'))
    print("inside delete conform")

    query="select * from gst_b2b_txn where b2b_id = %d"%(b2b_id)
    qs = b2b_txn.objects.raw(query)[0]
    if request.method == "POST":

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()

        query="delete from gst_b2b_txn where b2b_id=%d"%(b2b_id)
        print(query)
        try:
            cursor.execute(query)
            con.commit()
            pass
        except:
            con.rollback()

        return HttpResponseRedirect("/b2b/")
    context={
        'qs'  :qs,
    }

    return render(request,"b2b_del_con.html",context)

def about(request):
    context= {}
    return render(request,"about1.html",context)

def view_by_bussiness(request):
    form = Delete_business_form(request.POST)
    if request.method == "POST":
        temp  =  int(request.POST.get('gst_id'))

        con = MySQLdb.connect("localhost","root","root123","gst")
        cursor=con.cursor()
        query="select * from gst_businesses where gst_id = %d"%(temp)
        print(query)
        qs = businesses.objects.raw(query)[0]
        if qs:
            link="http://127.0.0.1:8000/view_by_bussiness/%d"%(temp)
            return redirect(link)
        else:
            return HttpResponseRedirect("/business/errors")
    heading="Select GST ID of the Business you wish to View Transaction"
    context={'form':form,'heading':heading}
    return render(request,"busdeleteform.html",context)

def view_con(request,*args,**kwargs):
    temp = int(kwargs.get('id'))
    query="select * from gst_b2c_txn where seller_gst_id =%d"%(temp)
    b2c_qs = b2c_txn.objects.raw(query)

    b2c_gst=0

    for obj in b2c_qs:
        b2c_gst=b2c_gst+obj.total_gst

    print(b2c_gst)
    query="select * from gst_b2b_txn where seller_gst_id =%d"%(temp)
    b2b_qs = b2b_txn.objects.raw(query)
    b2b_gst=0

    for obj in b2b_qs:
        b2b_gst=b2b_gst+obj.total_gst

    print(b2b_gst)

    gt_gst=b2c_gst+b2b_gst
    heading='Business Transaction Page '
    context={'heading':heading,'b2c_qs':b2c_qs,'b2b_qs':b2b_qs,'gt_gst':gt_gst,}
    return render(request,"bustxn.html",context)
