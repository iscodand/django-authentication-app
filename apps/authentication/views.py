from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get("password1"))
            new_user.save()
            messages.success(request, "User registered successfully!")
            return redirect('login')
        else:
            for value in form.errors.values():
                messages.error(request, f'{value}')

    form = SignUpForm()
    context = {'form': form}
    return render(request, 'authentication/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            if User.objects.filter(email=email).exists():
                username = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=username, password=password)

                if user is not None:
                        auth.login(request, user)
                        return redirect('home')
                else:
                    messages.error(request, "Incorrect e-mail / password! Verify and try again.")
                    return redirect('login')

            else:
                messages.error(request, 'User not found!')
                return redirect('login')
                
    form = LoginForm()
    context = {'form': form}
    return render(request, 'authentication/login.html', context)


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')
