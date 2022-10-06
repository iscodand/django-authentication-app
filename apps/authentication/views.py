from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('login')
        else:
            for value in form.errors.values():
                messages.error(request, f'{value}')

    form = SignUpForm()
    context = {'form': form}
    return render(request, 'authentication/signup.html', context)


def login(request):
    return render(request, 'authentication/login.html')


@login_required(login_url='/login')
def home(request):
    pass
