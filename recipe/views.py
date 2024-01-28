from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, RecipeItem
from item.models import Item



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

        return redirect('recipe')  # Перенаправлення на іншу сторінку, наприклад, список рецептів

    items = Item.objects.all()
    return render(request, 'recipe/createrecipe.html', {'items': items})


