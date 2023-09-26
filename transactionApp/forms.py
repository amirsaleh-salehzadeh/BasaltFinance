from django import forms
from accountApp.models import Account
from transactionApp.models import Transaction

class TransactionForm(forms.ModelForm):
    fromAccount = forms.ModelChoiceField(queryset=None, required=True, label="From Account")
    toAccount = forms.ModelChoiceField(queryset=None, required=True, label="To Account")
    TRANSACTION_CHOICES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    transactionType = forms.ChoiceField(choices=TRANSACTION_CHOICES, widget=forms.RadioSelect)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    
    class Meta:
        model = Transaction
        fields = ['fromAccount', 'toAccount', 'amount', 'transactionType']

    def __init__(self, user, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['fromAccount'].queryset = Account.objects.filter(user=user)
        self.fields['toAccount'].queryset = Account.objects.all()