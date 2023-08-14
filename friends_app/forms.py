from django import forms
from .models import Movie, Actor, Director, AudioTrack, CommentUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class SongsForm(forms.ModelForm):

    class Meta:

        model = AudioTrack
        fields = ['name_song', 'artist', 'song']
        labels = {
            'name_song': 'Название трека',
            'artist': 'Исполнитель',
            'song': 'Композиция'
        }


class AddPageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['director'].empty_label = 'Режиссер не выбран'

    class Meta:
        model = Movie
        fields = ['name', 'years', 'rating', 'content', 'slug', 'director', 'actors']
        labels = {
            'name': 'Название фильма',
            'years': 'Год производства',
            'rating': 'Рейтинг',
            'content': 'Описание фильма',
            'slug': 'URL',
            'director': 'Режиссер',
            'actors': 'Актеры фильма'
        }


class RegistrationForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2', 'email']


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CommentUserForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = CommentUser
        fields = ['name', 'comment']

        labels = {
            'name': 'Имя пользователя',
            'comment': 'Комментарий'
        }
        errors_message = {
            'name': {
                'required': 'Поле не должно быть пустым',
            },
            'comment': {
                'required': 'Не должно быть пустым'
            }
        }
