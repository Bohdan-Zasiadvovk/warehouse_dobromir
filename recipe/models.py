from django.db import models
from item.models import Item


class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    MEASURE_CHOICES = [
        ('gram', 'грам'),
        ('centimeter', 'сантиметр'),
        ('piece', 'штук')
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    measure = models.CharField(max_length=20, choices=MEASURE_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f"{self.item.name} -- {self.quantity} ({self.measure})"



