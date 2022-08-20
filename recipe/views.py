from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RegistrationForm, LoginForm, RecipeForm, IngredientForm, CategoryForm
from .models import Recipe, Ingredient, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Recipe




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
    print(recipe.ingredients.all())
    ingredients = recipe.ingredients.all()
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipe_detail.html', context)



"""view all ingredients"""
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    context = {
        'ingredients': ingredients,
    }
    return render(request, 'ingredient_list.html', context)

"""create new ingredient"""
def create_ingredient(request):
    form = IngredientForm()
    if request.method == "POST":
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            return redirect('ingredient_list')

    context = {
        "form": form,
    }
    return render(request, 'create_ingredient.html', context)

"""view all categories"""
def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'category_list.html', context)

"""add new category"""
def create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_list')

    context = {
        "form": form,
    }
    return render(request, 'create_category.html', context)




"""If you are the creator of the recipe, you can edit it"""
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = "__all__"
    template_name = 'update_recipe.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.user:
            return True
        return False

    def update_recipe(request, pk):
        recipe = Recipe.objects.get(pk=pk)
        form = RecipeForm(instance=recipe)
        if request.method == "POST":
            form = RecipeForm(request.POST, request.FILES, instance=recipe)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.save()
                return redirect('recipe_list')

        context = {
            "form": form,
            "pk": pk,
        }
        return render(request, 'update_recipe.html', context)