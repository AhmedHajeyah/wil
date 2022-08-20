from audioop import reverse
from email.mime import image
from unicodedata import category
from xml.dom import ValidationErr
from django.db import models

  
class Recipe(models.Model):
    """Recipe model"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    directions = models.TextField()
    servings = models.IntegerField()
    time_to_cook = models.IntegerField()
    calories = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=False)
    

    def __str__(self):
        return self.name

"""Each Increadiant is a ingredient in a recipe has category"""
    
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Ingredients'
        
"""list of categories for ingredients
one Ingredient can have many categories"""

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon= models.ImageField(upload_to='images/', blank=False)

    def __str__(self):
        return self.name
