from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Model):
    password = forms.CharField(label="Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget = forms.PasswordInput)

    class Meta():
        model = User
        fields = ['username', 'email']

