from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Warehouse, WarehouseItem, Item


def create_warehouse(request):
    if request.method == 'POST':
        warehouse = Warehouse.objects.create()
        return warehouse


def get_all_warehouses(request):
    if request.method == 'GET':
        warehouses = Warehouse.objects.all()
        return warehouses


def get_warehouse_by_id(request, warehouse_id):
    if request.method == 'GET':
        warehouse = Warehouse.objects.get(id=warehouse_id)
        return warehouse


def update_warehouse(request, warehouse_id, new_date):
    if request.method == 'PATCH':
        warehouse = Warehouse.objects.get(id=warehouse_id)
        warehouse.date = new_date
        warehouse.save()
        return warehouse


def delete_warehouse(request, warehouse_id):
    if request.method == 'DELETE':
        warehouse = Warehouse.objects.get(id=warehouse_id)
        warehouse.delete()


def add_warehouse_record_item(request, warehouse_id, item_id, measure, quantity):
    if request.method == 'POST':
        warehouse = Warehouse.objects.get(id=warehouse_id)
        item = Item.objects.get(id=item_id)

        warehouse_record_item = WarehouseItem.objects.create(
            warehouse=warehouse,
            item=item,
            measure=measure,
            quantity=quantity
        )
        return warehouse_record_item


def get_all_warehouse_record_items(request, warehouse_id):
    if request.method == 'GET':
        warehouse_record_items = WarehouseItem.objects.filter(warehouse_id=warehouse_id)
        return warehouse_record_items


def update_warehouse_record_item(request, warehouse_record_item_id, new_measure, new_quantity):
    if request.method == 'PATCH':
        warehouse_record_item = WarehouseItem.objects.get(id=warehouse_record_item_id)
        warehouse_record_item.measure = new_measure
        warehouse_record_item.quantity = new_quantity
        warehouse_record_item.save()
        return warehouse_record_item


def delete_warehouse_record_item(request, warehouse_record_item_id):
    if request.method == 'DELETE':
        warehouse_record_item = WarehouseItem.objects.get(id=warehouse_record_item_id)
        warehouse_record_item.delete()
