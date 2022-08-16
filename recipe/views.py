from django.shortcuts import render, redirect
from telnetlib import LOGOUT
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import RegistrationForm, LoginForm



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

def home(request):
    return render(request, 'home.html')
