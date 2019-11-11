from django.contrib import admin

from .models import StockItem, Deal

admin.site.register(StockItem)
admin.site.register(Deal)
