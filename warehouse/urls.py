from django.urls import path
from . import views


urlpatterns = [
    path('warehouse/', views.warehouse, name='warehouse'),
    path('warehouse/newinventory/', views.inventory, name='inventory'),
    path('warehouse/lastinventory/', views.edit_last_inventory, name='edit_last_inventory'),

]