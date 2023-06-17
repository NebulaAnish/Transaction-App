# user imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your forms here


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(
        max_length=254, help_text='Enter a valid email address')
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'avatar'
        ]


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField()
    bio = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'bio'
        ]
