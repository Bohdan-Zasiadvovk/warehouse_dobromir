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

from ingredient import views as ingredient_views
from package import views as package_views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('ingredient/', ingredient_views.ingredient, name='ingredient'),
    path('ingredient/create/', ingredient_views.create_ingredient, name='create_ingredient'),
    path('ingredient/all/', ingredient_views.get_all_ingredients, name='all_ingredients'),
    path('ingredient/update/<ingredient_id>/', ingredient_views.update_ingredient, name='update_ingredient'),
    path('ingredient/delete/<ingredient_id>/', ingredient_views.delete_ingredient, name='delete_ingredient'),

    path('package/', package_views.package, name='package'),
    path('package/create/', package_views.create_package, name='create_package'),
    path('package/all/', package_views.get_all_packages, name='all_packages'),
    path('package/update/<package_id>/', package_views.update_package, name='update_package'),
    path('package/delete/<package_id>/', package_views.delete_package, name='delete_package'),



]
