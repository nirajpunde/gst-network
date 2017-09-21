"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from dal import autocomplete
from django.contrib import admin
from django.views.generic import TemplateView
from gst import views
from django.urls import reverse

from gst.views import GST_idAutocomplete

urlpatterns = [
    url(r'^$',views.home),
    url(
        r'^gst-autocomplete/$',
        GST_idAutocomplete.as_view(),
        name='gst-autocomplete',
    ),
    url(r'^business/$',views.business),
    url(r'^business/create/$',views.create_business),
    url(r'^business/update/$',views.update_business),
    url(r'^business/update/confirm/(?P<id>[0-9]+)$',views.update_confirm),
    url(r'^business/delete/$',views.delete_business),
    url(r'^business/delete/confirm/(?P<id>[0-9]+)$',views.delete_confirm),
    url(r'^business/display/$',views.display),

    url(r'^product/$',views.product),
    url(r'^product/create/$',views.create_product),
    url(r'^product/update/$',views.update_product),
    url(r'^product/update/confirm/(?P<id>[0-9]+)$',views.product_update_confirm),
    url(r'^product/delete/$',views.delete_product),
    url(r'^product/delete/confirm/(?P<id>[0-9]+)$',views.delete_confirm),
    url(r'^product/display/$',views.productdisplay),

    url(r'^b2b/$',views.b2b),
    url(r'^b2b/add_txn/$',views.add_b2b_txn),
    url(r'^b2b/display_txn/$',views.display_b2b),
    url(r'^b2b/update_txn/$',views.update_b2b),
    url(r'^b2b/update/confirm/(?P<id>[0-9]+)$',views.b2b_update_confirm),
    url(r'^b2b/delete_txn/$',views.delete_b2b),
    url(r'^b2b/delete/confirm/(?P<id>[0-9]+)$',views.b2b_delete_confirm),

    url(r'^b2c/$',views.b2c),
    url(r'^b2c/add_txn/$',views.add_b2c_txn),
    url(r'^b2c/display_txn/$',views.display_b2c),
    url(r'^b2c/update_txn/$',views.update_b2c),
    url(r'^b2c/update/confirm/(?P<id>[0-9]+)$',views.b2c_update_confirm),
    url(r'^b2c/delete_txn/$',views.delete_b2c),
    url(r'^b2c/delete/confirm/(?P<id>[0-9]+)$',views.b2c_delete_confirm),


    url(r'^admin/', admin.site.urls),

]
