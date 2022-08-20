from unicodedata import category
from django.contrib import admin
from recipe.models import Recipe, Ingredient, Category

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Category)
