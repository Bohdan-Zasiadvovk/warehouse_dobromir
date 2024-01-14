from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Package


def create_package(request, name, measure):
    if request.method == 'POST':
        package = Package.objects.create(name=name, measure=measure)
        return package


def get_all_packages(request):
    if request.method == 'GET':
        packages = Package.objects.all()
        return packages


def get_package_by_id(request, package_id):
    if request.method == 'GET':
        package = Package.objects.get(id=package_id)
        return package


def update_package(request, package_id, new_name, new_measure):
    if request.method == 'PATCH':
        package = Package.objects.get(id=package_id)
        package.name = new_name
        package.measure = new_measure
        package.save()
        return package


def delete_package(request, package_id):
    if request.method == 'DELETE':
        package = Package.objects.get(id=package_id)
        package.delete()
