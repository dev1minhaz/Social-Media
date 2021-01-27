from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': "Email Address"}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': "Username"}))
    password1 = forms.CharField(
        required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': "Password"}))
    password2 = forms.CharField(
        required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': "Password(again)"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': "date"}))

    class Meta:
        model = UserProfile
        exclude = ('user',)
