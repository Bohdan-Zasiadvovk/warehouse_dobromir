from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.item, name='item'),
    path('item/create/', views.create_item, name='create_item'),
    path('item/all/', views.get_all_items, name='all_items'),
    path('item/update/<item_id>/', views.update_item, name='update_item'),
    path('item/delete/<item_id>/', views.delete_item, name='delete_item'),
]