from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CollectionItem

class CollectionItemForm(forms.ModelForm):
    class Meta:
        model = CollectionItem
        fields = ['title', 'description', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple()
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmailChangeForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Новый email")

    class Meta:
        model = User
        fields = ['email']