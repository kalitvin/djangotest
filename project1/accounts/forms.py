from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False, label="Имя")
    last_name = forms.CharField(required=False, label="Фамилия")
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(
        required=False,
        label="Аватар",
        widget=forms.FileInput,
    )
    class Meta:
        model = Profile
        fields = ("avatar", "bio", "location", "birth_date")
        labels = {
          "avatar": "avatar",
          "bio": "О себе",
          "location": "Город",
          "birth_date": "Дата рождения",
        }