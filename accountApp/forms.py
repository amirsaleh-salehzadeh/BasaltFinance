from django import forms
from .models import Account

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_name']
