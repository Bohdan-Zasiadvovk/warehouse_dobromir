from django.contrib import admin
from .models import Recipe, RecipeItem


admin.site.register(Recipe)
admin.site.register(RecipeItem)
