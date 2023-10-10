from django.contrib.auth.models import User
from django import forms
from bd.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm




class RegisterUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')


class LoginUserForms(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class Orders(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Product','date']