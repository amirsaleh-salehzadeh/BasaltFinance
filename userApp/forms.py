from django import forms
from .models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    username_validator = UnicodeUsernameValidator()
    default_validators = [username_validator]
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    username = forms.EmailField(error_messages={'required': 'Please enter a valid email address'}, validators=default_validators)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(False)
        user.email = user.username
        user = super().save()        
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
