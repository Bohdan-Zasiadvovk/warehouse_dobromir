from django import forms
from .models import Recipe, RecipeItem


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']


class RecipeItemForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = ['ingredient', 'measure', 'quantity']