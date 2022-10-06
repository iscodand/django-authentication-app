from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validation import *


class SignUpForm(UserCreationForm):
    error_css_class = 'error'
    required_css_class = 'required'
    
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']

