from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Recipe, RecipeItem, Ingredient


def create_recipe(request, name):
    if request.method == 'POST':
        recipe = Recipe.objects.create(name=name)
        return recipe


def get_all_recipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        return recipes


def get_recipe_by_id(request, recipe_id):
    if request.method == 'GET':
        recipe = Recipe.objects.get(id=recipe_id)
        return recipe


def update_recipe(request, recipe_id, new_name):
    if request.method == 'PATCH':
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.name = new_name
        recipe.save()
        return recipe


def delete_recipe(request, recipe_id):
    if request.method == 'DELETE':
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.delete()


def add_recipe_item(request, recipe_id, ingredient_id, measure, quantity):
    if request.method == 'POST':
        recipe = Recipe.objects.get(id=recipe_id)
        ingredient = Ingredient.objects.get(id=ingredient_id)

        recipe_item = RecipeItem.objects.create(
            recipe=recipe,
            ingredient=ingredient,
            measure=measure,
            quantity=quantity
        )
        return recipe_item


def get_all_recipe_items(request, recipe_id):
    if request.method == 'GET':
        recipe_items = RecipeItem.objects.filter(recipe_id=recipe_id)
        return recipe_items


def update_recipe_item(request, recipe_item_id, new_measure, new_quantity):
    if request.method == 'PATCH':
        recipe_item = RecipeItem.objects.get(id=recipe_item_id)
        recipe_item.measure = new_measure
        recipe_item.quantity = new_quantity
        recipe_item.save()
        return recipe_item


def delete_recipe_item(request, recipe_item_id):
    if request.method == 'DELETE':
        recipe_item = RecipeItem.objects.get(id=recipe_item_id)
        recipe_item.delete()
