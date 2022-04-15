from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Имя')
    last_name = forms.CharField(max_length=100, required=True, label='Фамилия')
    email = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com')
    phone = forms.RegexField(max_length=10, regex=r'^\+?1?\d{9,15}$', label='Телефон')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')

        def clean_email(self):
            cd = self.cleaned_data
            if User.objects.get(email=cd['email']):
                raise forms.ValidationError('User with such mail exists. Use another.')
            return cd['email']