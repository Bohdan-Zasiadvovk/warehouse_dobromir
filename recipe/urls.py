from django.urls import path
from . import views


urlpatterns = [
    path('recipe/', views.recipe, name='recipe'),
    # path('recipe/create/', views.create_recipe, name='create_recipe'),
]
