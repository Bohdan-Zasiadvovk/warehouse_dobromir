from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Container


def create_container(request, name, measure):
    if request.method == "POST":
        container = Container.objects.create(name=name, measure=measure)
        return container


def get_all_containers(request):
    if request.method == "GET":
        containers = Container.objects.all()
        return containers


def get_container_by_id(request, container_id):
    if request.method == "GET":
        container = Container.objects.get(id=container_id)
        return container


def update_container(request, container_id, new_name, new_measure):
    if request.method == "PATCH":
        container = Container.objects.get(id=container_id)
        container.name = new_name
        container.measure = new_measure
        container.save()
        return container


def delete_container(request, container_id):
    if request.method == "DELETE":
        container = Container.objects.get(id=container_id)
        container.delete()
