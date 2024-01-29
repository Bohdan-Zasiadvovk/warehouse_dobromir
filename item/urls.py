from django.urls import path
from . import views

urlpatterns = [
    path('', views.item, name='item'),
    path('create/', views.create_item, name='create_item'),
    path('all/', views.get_all_items, name='all_items'),
    path('update/<item_id>/', views.update_item, name='update_item'),
    path('delete/<item_id>/', views.delete_item, name='delete_item'),
]