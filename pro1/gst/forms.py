from .models import businesses,products,b2c_txn,b2b_txn
from django import forms
from dal import autocomplete
#class create_business(forms.Form)
class Businessform(forms.Form):
        acc_no     = forms.IntegerField()
        bus_name   = forms.CharField()
        email_id   = forms.EmailField()
        phone_no   = forms.IntegerField()
        hq_address = forms.CharField()
        #prod_count = forms.IntegerField()
        #turnover = forms.PositiveIntegerField(null=False)
        sector = forms.CharField()

class Update_business_form(forms.Form):
    gst_id = forms.ModelChoiceField(
    queryset=businesses.objects.all()
    )

class Upconbusform(forms.Form):
        acc_no     = forms.IntegerField()
        bus_name   = forms.CharField()
        email_id   = forms.EmailField()
        phone_no   = forms.IntegerField()
        hq_address = forms.CharField()
        #prod_count = forms.IntegerField()
        #turnover = forms.PositiveIntegerField(null=False)
        sector = forms.CharField()

class Delete_business_form(forms.Form):
    gst_id = forms.ModelChoiceField(
    queryset=businesses.objects.all()
    )

class Productform(forms.Form):

    prod_name = forms.CharField()
    #hsn = forms.IntegerField(null=False,unique=True,default=0)

    prod_make = forms.CharField()
    prod_type = forms.CharField()

    manuf_price = forms.IntegerField()
    sell_price = forms.IntegerField()

    manufacturer = forms.ModelChoiceField(
    queryset=businesses.objects.all()
    )
    applied_gst = forms.IntegerField()

class Update_product_form(forms.Form):
    prod_id = forms.ModelChoiceField(
    queryset=products.objects.all()
    )

class product_update_conf(forms.Form):

    prod_name = forms.CharField()
    #hsn = forms.IntegerField(null=False,unique=True,default=0)

    prod_make = forms.CharField()
    prod_type = forms.CharField()

    manuf_price = forms.IntegerField()
    sell_price = forms.IntegerField()

    manufacturer = forms.ModelChoiceField(
    queryset=businesses.objects.all(),
    to_field_name="gst_id"
    )
    applied_gst = forms.IntegerField()

class delete_product_form(forms.Form):
    prod_id = forms.ModelChoiceField(
    queryset=products.objects.all()
    )

class b2c_txn_create(forms.Form):
    prod_id = forms.ModelChoiceField(
    queryset=products.objects.all()
    )

    seller_gst = forms.ModelChoiceField(
    queryset=businesses.objects.all(),
    to_field_name="gst_id"
    )
    quantity = forms.IntegerField()

class update_b2c_form(forms.Form):
    b2c_id = forms.ModelChoiceField(
    queryset=b2c_txn.objects.all()
    )

class delete_b2c_form(forms.Form):
    b2c_id = forms.ModelChoiceField(
    queryset=b2c_txn.objects.all()
    )

class b2b_txn_create(forms.Form):
    prod_id = forms.ModelChoiceField(
    queryset=products.objects.all()
    )
    buyer_gst = forms.ModelChoiceField(
    queryset=businesses.objects.all(),
    to_field_name="gst_id"
    )
    seller_gst = forms.ModelChoiceField(
    queryset=businesses.objects.all(),
    to_field_name="gst_id"
    )

    quantity = forms.IntegerField()

class update_b2b_form(forms.Form):
    b2b_id = forms.ModelChoiceField(
    queryset=b2b_txn.objects.all()
    )

class delete_b2b_form(forms.Form):
    b2b_id= forms.ModelChoiceField(
    queryset=b2b_txn.objects.all()
    )
