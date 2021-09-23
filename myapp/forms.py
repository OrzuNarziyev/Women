from django import forms
from .models import *


class WomenForms(forms.ModelForm):

    class Meta:
        model = Women
        fields = '__all__'
