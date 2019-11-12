from django.contrib import admin

from .models import StockItem, Deal, Partner

admin.site.register(StockItem)
admin.site.register(Deal)
admin.site.register(Partner)
