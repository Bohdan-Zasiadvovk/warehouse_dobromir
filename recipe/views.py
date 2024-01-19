from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm, RecipeItemForm
from .models import Recipe, RecipeItem


def recipe(request):
    return render(request, 'recipe/recipe.html')


def create_recipe(request):
    if request.method == 'GET':
        return render(request, 'recipe/createrecipe.html', {'form': RecipeForm()})
    else:
        try:
            form = RecipeForm(request.POST)
            new_recipe = form.save(commit=False)
            new_recipe.save()
            return redirect('all_recipes')
        except ValueError:
            return render(request, 'recipe/createrecipe.html', {'form': RecipeForm(), 'error': 'Bad data passed in. Try again'})


def get_all_recipes(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        return render(request, 'recipe/allrecipes.html', {'recipes': recipes})


def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "GET":
        return render(request, 'recipe/updaterecipe.html', {'recipe': recipe, 'form': RecipeForm(instance=recipe)})
    else:
        try:
            form = RecipeForm(request.POST, instance=recipe)
            form.save()
            return redirect('all_recipes')
        except ValueError:
            return render(request, 'recipe/updaterecipe.html', {'recipe': recipe, 'form': RecipeForm(instance=recipe)})


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('all_recipes')


def create_recipe_item(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'GET':
        return render(request, 'recipe/createrecipeitem.html', {'form': RecipeItemForm(), 'recipe': recipe})

    else:
        try:
            form = RecipeItemForm(request.POST)
            recipe_item = form.save(commit=False)
            recipe_item.recipe_item = recipe
            recipe_item.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
        except ValueError:
            return render(request, 'recipe/createrecipeitem.html', {'form': RecipeItemForm(),  'error': 'Bad data passed in. Try again'})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipedetail.html', {'recipe': recipe})


def update_recipe_item(request, recipe_id, recipe_item_id):
    recipe_item = get_object_or_404(RecipeItem, id=recipe_item_id)
    if request.method == "GET":
        return render(request, 'recipe/updaterecipeitem.html', {'recipeitem': recipe_item, 'form': RecipeItemForm(instance=recipe_item)})
    else:
        try:
            form = RecipeItemForm(request.POST, instance=recipe_item)
            form.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
        except ValueError:
            return render(request, 'recipe/updaterecipeitem.html', {'recipeitem': recipe_item, 'form': RecipeItemForm(instance=recipe_item)})


def delete_recipe_item(request, recipe_id, recipe_item_id):
    recipe_item = get_object_or_404(RecipeItem, id=recipe_item_id)

    if request.method == 'POST':
        recipe_item.delete()
        return redirect('recipe_detail', recipe_id=recipe_id)
