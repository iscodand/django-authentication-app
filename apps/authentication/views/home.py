from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return redirect('signup')


@login_required(login_url='/login')
def home(request):
    return render(request, 'home/home.html')
