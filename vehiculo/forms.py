from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    add_vehiculomodel = forms.BooleanField(
        required=False,
        label='Es staff'
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")