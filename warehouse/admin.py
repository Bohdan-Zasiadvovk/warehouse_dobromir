from django.contrib import admin
from .models import Warehouse, WarehouseItem


admin.site.register(Warehouse)
admin.site.register(WarehouseItem)
