from django import forms
from django.contrib.auth.models import User
from django.core import validators




class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید', 'class': 'fadeIn second'}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'class': 'fadeIn second'}),
        label='کلمه ی عبور'
    )


