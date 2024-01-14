from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .forms import IngredientForm
from .models import Ingredient


def create_ingredient(request):
    if request.method == 'GET':
        return render(request, 'ingredient/createingredient.html', {'form': IngredientForm()})
    else:
        try:
            form = IngredientForm(request.POST)
            new_ingredient = form.save(commit=False)
            new_ingredient.save()
            return redirect('get_all_ingredients')
        except ValueError:
            return render(request, 'ingredient/createingredient.html', {'form': IngredientForm(), 'error': 'Bad data passed in. Try again'})


def get_all_ingredients(request):
    if request.method == "GET":
        ingredients = Ingredient.objects.all()
        return render(request, 'ingredient/allingredients.html', {'ingredients': ingredients})


# def get_ingredient_by_id(request, ingredient_id):
#     if request.method == "GET":
#         ingredient = Ingredient.objects.get(id=ingredient_id)
#         return ingredient


def update_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('get_all_ingredients')
    else:
        form = IngredientForm(instance=ingredient)

    return render(request, 'ingredient/updateingredient.html', {'form': form, 'ingredient': ingredient})


def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    if request.method == 'POST':
        ingredient.delete()
        return redirect('get_all_ingredients')