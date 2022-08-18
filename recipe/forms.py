from datetime import datetime
from email.mime import image
from email.policy import default
from django import forms
from django.contrib.auth import get_user_model
from .models import Recipe, Ingredient


User = get_user_model()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password','first_name','last_name')
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'instructions', 'servings', 'time_to_cook', 'calories', 'image', 'ingredients', 'directions')
        widgets = {
            "image": forms.FileInput(),
            'ingredients': forms.SelectMultiple(),
        }

