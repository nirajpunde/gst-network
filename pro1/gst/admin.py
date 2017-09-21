# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import businesses
from .models import products
from .models import b2b_txn
from .models import b2c_txn


admin.site.register(businesses)
admin.site.register(products)
admin.site.register(b2b_txn)
admin.site.register(b2c_txn)
