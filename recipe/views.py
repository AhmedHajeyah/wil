from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .forms import RegistrationForm, LoginForm, RecipeForm
from .models import Recipe, Ingredient



# Create your views here.


def register_user(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect('home')

    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

def login_user(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    context = {
        "form": form,
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

# def home(request):
#     return render(request, 'home.html')


def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_list.html', context)

class RecipeView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 5
    queryset = Recipe.objects.all()


def create_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('home')

    context = {
        "form": form,
    }
    return render(request, 'create_recipe.html', context)



def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)

    
# def ingredients_list(request):
#     ingredients = Ingredient.objects.all()
#     context = {
#         'ingredients': ingredients
#     }
#     return render(request, 'ingredients_list.html', context)

"""Show Ingredients in a Recipe"""
def ingredient_loop(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.all()
    context = {
        'ingredients': ingredients
    }
    return render(request, 'recipe_detail.html', context)