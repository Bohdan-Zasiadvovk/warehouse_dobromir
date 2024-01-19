from django.db import models
from ingredient.models import Ingredient


class Warehouse(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class WarehouseItem(models.Model):
    item = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    warehouse_record_item = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    measure = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f"{self.item.name} -- {self.quantity} ({self.measure})"
