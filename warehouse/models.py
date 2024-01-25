from django.db import models
from item.models import Item


class Warehouse(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date


class WarehouseItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    warehouse_item = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f"{self.item.name} -- {self.quantity}"
