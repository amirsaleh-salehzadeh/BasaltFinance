from django.shortcuts import render, redirect
from userApp.forms import UserRegistrationForm
from accountApp.models import Account
from transactionApp.models import Transaction
from accountApp.forms import AccountCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    num_accounts = Account.objects.all().count()
    my_accounts = Account.objects.filter(user = request.user).count()
    fromAccs = Account.objects.filter(user = request.user)
    my_transactions = Transaction.objects.filter(
        fromAccount__in=fromAccs
    ).count()
    num_transactions = Transaction.objects.all().count()
    context = {
        'num_accounts': num_accounts,
        'num_transactions': num_transactions,
        'my_accounts': my_accounts,
        'my_transactions': my_transactions
        }
    return render(request, 'index.html', context)

@login_required
def accounts_lists(request):
    accounts = Account.objects.filter(user = request.user)  # Get all accounts
    return render(request, 'account/account_list.html', {'accounts': accounts})

@login_required
def account_create(request):
    form = AccountCreationForm()
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user  # Assign the current user
            account.save()
            return redirect('accountApp:account_list')
    return render(request, 'account/account_create.html', {'form': form})
