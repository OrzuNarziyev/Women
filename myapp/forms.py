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
    class Meta:
        model = User
        fields = ['username','password1','password2','email']




