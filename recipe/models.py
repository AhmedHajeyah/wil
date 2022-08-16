from audioop import reverse
from email.mime import image
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
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Ingredients'
        