from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from item.models import Item
from .models import Recipe, RecipeItem


def recipe(request):
    return render(request, 'recipe/recipe.html')


def create_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        items = request.POST.getlist('item')
        measures = request.POST.getlist('measure')
        quantities = request.POST.getlist('quantity')

        recipe = Recipe.objects.create(name=recipe_name)

        for item, measure, quantity in zip(items, measures, quantities):
            item_obj = Item.objects.get(pk=item)
            RecipeItem.objects.create(recipe=recipe, item=item_obj, measure=measure, quantity=quantity)

        return redirect('all_recipes')

    items = Item.objects.all()
    context = {'items': items, "measures": []}
    measure_items = RecipeItem.MEASURE_CHOICES
    for measure in measure_items:
        context["measures"].append(list(measure))
    return render(request, 'recipe/createrecipe.html', context)


def all_recipes(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        context = {'recipes': recipes}
        return render(request, 'recipe/allrecipes.html', context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe_items = RecipeItem.objects.filter(recipe=recipe)

    context = {'recipe': recipe, 'recipe_items': recipe_items}
    return render(request, 'recipe/recipedetail.html', context)


def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        items = request.POST.getlist('item')
        measures = request.POST.getlist('measure')
        quantities = request.POST.getlist('quantity')

        if not recipe_name:
            # Обробка помилки, наприклад, повернення на ту ж сторінку з повідомленням про помилку
            recipe_items = recipe.recipeitem_set.all()
            items = Item.objects.all()
            context = {'recipe': recipe, 'recipe_items': recipe_items, 'items': items, "measures": [],
                       'error_message': 'Назва рецепту не може бути порожньою'}
            measure_items = RecipeItem.MEASURE_CHOICES
            for measure in measure_items:
                context["measures"].append(list(measure))
            return render(request, 'recipe/updaterecipe.html', context)

        # Оновлення існуючого рецепту
        recipe.name = recipe_name
        recipe.save()

        # Очищення існуючих RecipeItem для даного рецепту
        recipe.recipeitem_set.all().delete()

        # Додавання нових RecipeItem
        for item, measure, quantity in zip(items, measures, quantities):
            item_obj = Item.objects.get(pk=item)
            RecipeItem.objects.create(recipe=recipe, item=item_obj, measure=measure, quantity=quantity)

        delete_item_id = request.POST.get('delete_item_id')
        if delete_item_id:
            RecipeItem.objects.filter(id=delete_item_id).delete()

        return redirect('all_recipes')

    # Отримання існуючих RecipeItem для рецепту
    recipe_items = recipe.recipeitem_set.all()

    items = Item.objects.all()
    context = {'recipe': recipe, 'items': items, 'measures': [], 'recipe_items': recipe_items}
    measure_items = RecipeItem.MEASURE_CHOICES
    for measure in measure_items:
        context["measures"].append(list(measure))
    return render(request, 'recipe/updaterecipe.html', context)


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('all_recipes')  # Перенаправлення на список рецептів

    return HttpResponse("Метод GET не підтримується для цієї сторінки.")
