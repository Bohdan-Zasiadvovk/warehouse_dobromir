from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipe, name='recipe'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('all', views.all_recipes, name='all_recipes'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('<int:recipe_id>/update/', views.update_recipe, name='update_recipe'),
    path('<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    # path('<int:recipe_id>/deleterecipeitem/<int:recipe_item_id>/', views.delete_recipe_item, name='delete_recipe_item'),

]
