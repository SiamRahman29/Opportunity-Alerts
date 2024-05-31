from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):


    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full  py-4 px-6 rounded-xl',
        'placeholder': "Your Username",
                
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full  py-4 px-6 rounded-xl ',
        'placeholder': "Your Password",
                
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full  py-4 px-6 rounded-xl ',
        'placeholder': "Your Username",
                
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Your Email Address",
        'class': 'w-full  py-4 px-6 rounded-xl',
                        
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full  py-4 px-6 rounded-xl ',
        'placeholder': 'Your Password',
                
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full  py-4 px-6 rounded-xl ',
        'placeholder': "Repeat Password",
                
    }))