"""
URL configuration for warehouse_dobromir project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from item import views as item_views
from recipe import views as recipe_views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', TemplateView.as_view(template_name='home.html'), name='home'),


    path('item/', item_views.item, name='item'),
    path('item/create/', item_views.create_item, name='create_item'),
    path('item/all/', item_views.get_all_items, name='all_items'),
    path('item/update/<item_id>/', item_views.update_item, name='update_item'),
    path('item/delete/<item_id>/', item_views.delete_item, name='delete_item'),



    path('recipe/', recipe_views.recipe, name='recipe'),
    path('recipe/create/', recipe_views.create_recipe, name='create_recipe'),
    path('recipe/all/', recipe_views.get_all_recipes, name='all_recipes'),
    path('recipe/update/<recipe_id>/', recipe_views.update_recipe, name='update_recipe'),
    path('recipe/delete/<recipe_id>/', recipe_views.delete_recipe, name='delete_recipe'),
    path('recipe/<recipe_id>/', recipe_views.recipe_detail, name='recipe_detail'),
    path('recipe/<recipe_id>/additem/', recipe_views.create_recipe_item, name='create_recipe_item'),
    path('recipe/<recipe_id>/updateitem/<recipe_item_id>/', recipe_views.update_recipe_item, name='update_recipe_item'),
    path('recipe/<recipe_id>/deleteitem/<recipe_item_id>/', recipe_views.delete_recipe_item, name='delete_recipe_item'),

]
