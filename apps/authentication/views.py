from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('login')
        else:
            for value in form.errors.values():
                messages.error(request, f'{value}')

    return render(request, 'authentication/signup.html', {'form': form})


def login(request):
    form = LoginForm(request.POST or None)
    
    return render(request, 'authentication/login.html')


@login_required(login_url='/login')
def home(request):
    pass
