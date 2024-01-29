from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_recipe, name='create_recipe'),
    # path('create/', views.create_recipe, name='create_recipe'),
]
