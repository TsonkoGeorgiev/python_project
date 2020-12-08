from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from bike_auth.models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


