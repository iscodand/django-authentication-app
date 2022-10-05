from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validation import *


class SignUpForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        error_list = dict()

        verify_empty_fields(first_name, 'first_name', error_list)
        verify_empty_fields(last_name, 'last_name', error_list)

        if error_list is not None:
            for error in error_list:
                error_message = error_list[error]
                self.add_error(error, error_message)

        return self.cleaned_data
