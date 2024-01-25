from django.contrib import admin
from .models import Warehouse, WarehouseItem


class WarehouseItemInline(admin.TabularInline):
    model = WarehouseItem


class WarehouseAdmin(admin.ModelAdmin):
    inlines = [WarehouseItemInline]


admin.site.register(Warehouse, WarehouseAdmin)
