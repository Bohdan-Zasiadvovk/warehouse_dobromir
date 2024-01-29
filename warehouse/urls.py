from django.urls import path
from . import views


urlpatterns = [
    path('', views.warehouse, name='warehouse'),
    path('newinventory/', views.inventory, name='inventory'),
    path('lastinventory/', views.edit_last_inventory, name='edit_last_inventory'),

]