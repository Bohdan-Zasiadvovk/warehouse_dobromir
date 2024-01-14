from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Ingredient


def create_ingredient(request, name, measure):
    if request.method == "POST":
        ingredient = Ingredient.objects.create(name=name, measure=measure)
        return ingredient


def get_all_ingredients(request):
    if request.method == "GET":
        ingredients = Ingredient.objects.all()
        return ingredients


def get_ingredient_by_id(request, ingredient_id):
    if request.method == "GET":
        ingredient = Ingredient.objects.get(id=ingredient_id)
        return ingredient


def update_ingredient(request, ingredient_id, new_name, new_measure):
    if request.method == "PATCH":
        ingredient = Ingredient.objects.get(id=ingredient_id)
        ingredient.name = new_name
        ingredient.measure = new_measure
        ingredient.save()
        return ingredient


def delete_ingredient(request, ingredient_id):
    if request.method == "DELETE":
        ingredient = Ingredient.objects.get(id=ingredient_id)
        ingredient.delete()
