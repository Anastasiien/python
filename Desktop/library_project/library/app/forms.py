from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CollectionItem
from django import forms
from .models import CollectionItem, Genre

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

class CollectionItemForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    new_genre = forms.CharField(
        max_length=100,
        required=False,
        label="Add a genre"
    )

    class Meta:
        model = CollectionItem
        fields = ['title', 'description', 'genres', 'new_genre']