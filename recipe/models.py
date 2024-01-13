from django.db import models
from ingredient.models import Ingredient


class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe_item = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    measure = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f"{self.ingredient.name} -- {self.quantity} ({self.measure})"



