from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CollectionItem, Genre

class CollectionItemForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Выберите жанры"
    )

    new_genre = forms.CharField(
        max_length=100,
        required=False,
        label="Добавить новый жанр",
        help_text="Введите название нового жанра, если его нет в списке выше"
    )

    class Meta:
        model = CollectionItem
        fields = ['title', 'description', 'genres', 'new_genre']
        labels = {
            'title': 'Название',
            'description': 'Описание',
        }
        help_texts = {
            'title': 'Обязательное поле. Краткое название элемента коллекции.',
            'description': 'Необязательное поле. Подробное описание элемента.',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        help_texts = {
            'username': 'Обязательное поле. Только буквы, цифры и символы @.+-_.',
        }


class EmailChangeForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Новый email")

    class Meta:
        model = User
        fields = ['email']