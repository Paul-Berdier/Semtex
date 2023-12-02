from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
