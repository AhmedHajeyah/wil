from django.contrib import admin
from recipe.models import Recipe, Ingredient

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
