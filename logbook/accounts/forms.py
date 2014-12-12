from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import User


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.CharField(label='Email')

    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email", "username", "password1",
            "password2",
        )

class AuthenticateUserForm(AuthenticationForm):

    def confirm_login_allowed(self, user):
        pass