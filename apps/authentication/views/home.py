from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.forms import PasswordChangeForm


def index(request):
    return redirect('signup')


@login_required(login_url='/login')
def home(request):
    return render(request, 'home/home.html')


@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            auth.update_session_auth_hash(request, user)
            messages.success(request, 'Your password was succesfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Ops, an error ocurred! Please, try again :)')

    form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'home/change_password/change_password.html', context)
