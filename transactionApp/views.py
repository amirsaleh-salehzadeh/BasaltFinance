from django.shortcuts import render, redirect
from transactionApp.models import Transaction
from transactionApp.forms import TransactionForm
from accountApp.models import Account
from django.contrib.auth.decorators import login_required

@login_required
def search_transactions(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')  # Get the search query from the URL parameter
        transactions = Transaction.objects.filter(transaction_type__icontains=query)
        return render(request, 'wallet/search_transactions.html', {'transactions': transactions})
@login_required
def transaction_list(request):
    user_accounts = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(fromAccount__in = user_accounts).union(
        Transaction.objects.filter(
            toAccount__in=user_accounts
        )
    )
    return render(request, 'transaction/transaction_list.html', {'transactions': transactions})

@login_required
def create_transaction(request):
    form = TransactionForm(request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()
            return redirect('transactionApp:transaction_list')  # Redirect to a transaction list page or another page
    return render(request, 'transaction/transaction_create.html', {'form': form})