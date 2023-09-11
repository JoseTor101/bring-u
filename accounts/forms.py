from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'name', 'last_name', 'tel', 'profile_pic', 'password1', 'password2')
    