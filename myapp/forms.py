from django import forms
from .models import *

# authentications
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class WomenForms(forms.ModelForm):
    class Meta:
        model = Women
        fields = '__all__'


class CreateUserForm(UserCreationForm):

    username = forms.CharField(label="Username", required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20','placeholder':'Foydalanuvchi'}))
    password1 = forms.CharField(label="Parol", required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    password2 = forms.CharField(label="Takroriy parol", required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    email = forms.EmailField(label="Email", required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20'}))

    class Meta:
        model = User

        fields = ['username', 'password1', 'password2', 'email']


