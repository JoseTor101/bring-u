from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    tel = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('name','username', 'email', 'password1', 'password2', 'tel')

