from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import AdditionalProduct


def create_additional_product(request, name, measure):
    if request.method == "POST":
        additional_product = AdditionalProduct.objects.create(name=name, measure=measure)
        return additional_product


def get_all_additional_products(request):
    if request.method == "GET":
        additional_products = AdditionalProduct.objects.all()
        return additional_products


def get_additional_product_by_id(request, product_id):
    if request.method == "GET":
        additional_product = AdditionalProduct.objects.get(id=product_id)
        return additional_product


def update_additional_product(request, product_id, new_name, new_measure):
    if request.method == "PATCH":
        additional_product = AdditionalProduct.objects.get(id=product_id)
        additional_product.name = new_name
        additional_product.measure = new_measure
        additional_product.save()
        return additional_product


def delete_additional_product(request, product_id):
    if request.method == "DELETE":
        additional_product = AdditionalProduct.objects.get(id=product_id)
        additional_product.delete()
