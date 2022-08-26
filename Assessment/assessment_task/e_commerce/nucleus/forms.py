from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ("date_joined", "last_login", "superuser_status", "staff_status", "active", "password",
                   )


# class UserRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ("groups", "superuser_status", 'user_permissions', 'date_joined')
#
#         widgets = {
#             "password": forms.PasswordInput(),
#
#         }
