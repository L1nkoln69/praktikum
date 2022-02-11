from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth import get_user


class CreatePosts(forms.ModelForm):
    is_published = forms.BooleanField(label='Опубликовать')

    class Meta:
        model = Post
        fields = ['title', 'short_description', 'image', 'description', 'is_published']


class ToAdminForm(forms.Form):
    text = forms.CharField(label='Text', widget=forms.Textarea)
    email = forms.EmailField(label='Email')


class RegistrUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
