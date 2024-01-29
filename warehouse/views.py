from django.shortcuts import render, redirect, get_object_or_404
from .models import Warehouse, WarehouseItem, Item
from .forms import InventoryForm


def warehouse(request):
    return render(request, 'warehouse/warehouse.html')


def inventory(request):

    items = Item.objects.order_by('category', 'name')

    if request.method == 'POST':
        form = InventoryForm(request.POST, items=items)
        if form.is_valid():
            warehouse_instance = Warehouse.objects.create()
            for item in items:
                quantity = form.cleaned_data.get(f'item_{item.id}')
                WarehouseItem.objects.create(
                    item=item,
                    warehouse_item=warehouse_instance,
                    quantity=quantity
                )

                # Оновити кількість для всіх item одразу
                item.quantity = quantity
                item.save()

            return redirect('warehouse')
    else:
        form = InventoryForm(items=items)

        return render(request, 'warehouse/inventory.html', {'form': form, 'items': items})



def edit_last_inventory(request):
    last_warehouse_instance = Warehouse.objects.order_by('-date').first()


    # Отримати всі товари, пов'язані з останньою інвентаризацією
    warehouse_items = WarehouseItem.objects.filter(warehouse_item=last_warehouse_instance)
    items = Item.objects.order_by('category', 'name')

    # Створити словник для ініціалізації форми
    initial_data = {'item_' + str(item.id): warehouse_item.quantity for item, warehouse_item in
                    zip(items, warehouse_items)}

    if request.method == 'GET':
        form = InventoryForm(items=items, initial=initial_data)

        return render(request, 'warehouse/editlastinventory.html', {'form': form, 'items': items})

    else:
        form = InventoryForm(request.POST, items=items, initial=initial_data)
        if form.is_valid():
            for item, warehouse_item in zip(items, warehouse_items):
                quantity = form.cleaned_data.get('item_' + str(item.id))
                warehouse_item.quantity = quantity
                warehouse_item.save()

            return redirect('warehouse')
