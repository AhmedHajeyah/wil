"""whatilove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from recipe import views
from django.conf import settings
from django.conf.urls.static import static
from recipe.models import Recipe



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home, name='home'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('recipe_detail/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('ingredient_list/', views.ingredient_list, name='ingredient_list'),
    path('create_ingredient/', views.create_ingredient, name='create_ingredient'),
    path('category_list/', views.category_list, name='category_list'),
    path('create_category/', views.create_category, name='create_category'),
    path('update_recipe/<int:pk>/', views.RecipeUpdateView.as_view(), name='update_recipe'),
    path('delete_recipe/<int:pk>/', views.delete_recipe, name='delete_recipe'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
