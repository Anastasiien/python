from django import forms
from .models import CollectionItem

class CollectionItemForm(forms.ModelForm):
    class Meta:
        model = CollectionItem
        fields = ['title', 'description', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple()  # для выбора нескольких жанров
        }
