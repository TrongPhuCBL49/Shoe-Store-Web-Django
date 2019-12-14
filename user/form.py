from django import forms
from .models import CustomerUser

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Username'",
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'onfocus': "this.placeholder = ''",
            'onblur': "this.placeholder = 'Password'",
        }
    ))
        