from django.shortcuts import render, redirect, get_object_or_404
from .forms import IngredientForm
from .models import Ingredient


def ingredient(request):
    return render(request, 'ingredient/ingredient.html')


def create_ingredient(request):
    if request.method == 'GET':
        return render(request, 'ingredient/createingredient.html', {'form': IngredientForm()})
    else:
        try:
            form = IngredientForm(request.POST)
            new_ingredient = form.save(commit=False)
            new_ingredient.save()
            return redirect('all_ingredients')
        except ValueError:
            return render(request, 'ingredient/createingredient.html', {'form': IngredientForm(), 'error': 'Bad data passed in. Try again'})


def get_all_ingredients(request):
    if request.method == "GET":
        ingredients = Ingredient.objects.all()
        return render(request, 'ingredient/allingredients.html', {'ingredients': ingredients})


def update_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == "GET":
        return render(request, 'ingredient/updateingredient.html', {'ingredient': ingredient, 'form': IngredientForm(instance=ingredient)})
    else:
        try:
            form = IngredientForm(request.POST, instance=ingredient)
            form.save()
            return redirect('all_ingredients')

        except ValueError:
            return render(request, 'ingredient/updateingredient.html', {'ingredient': ingredient, 'form': IngredientForm(instance=ingredient)})


def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    if request.method == 'POST':
        ingredient.delete()
        return redirect('all_ingredients')

