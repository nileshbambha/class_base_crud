from django import forms
from .models import emp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class empForm(forms.ModelForm):
    
    class Meta:
        model = emp
        fields = ("name","image","age","gender")

class signin(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',]


class Subscribe(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email