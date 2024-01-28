from django.contrib import admin
from .models import Recipe, RecipeItem


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeItemInline]


admin.site.register(Recipe, RecipeAdmin)
