from django import forms
from django.contrib.auth.models import User
from .validation import *
from django.contrib.auth.forms import AuthenticationForm 


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget = forms.PasswordInput)

    class Meta():
        model = User
        fields = ['username', 'email']
        
    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        error_list = dict()
        
        verify_password(field_name='password1', password1=password1, password2=password2, error_list=error_list)
        
        if User.objects.filter(email=email).exists():
            error_list['email'] = 'Email already registered!'
        
        if User.objects.filter(username=username).exists():
            error_list['email'] = 'Username already registered!'

        if error_list is not None:
            for error in error_list:
                error_message = error_list[error]
                self.add_error(error, error_message)
                
        return self.cleaned_data
    
    
class LoginForm(forms.ModelForm):
    username_or_email = forms.CharField(label="Username or Email", widget = forms.CharField)
    password = forms.CharField(label="Password", widget = forms.PasswordInput)
