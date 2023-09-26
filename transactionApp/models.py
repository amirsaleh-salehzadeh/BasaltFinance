from django.db import models
from accountApp.models import Account

class Transaction(models.Model):
    transactionId = models.AutoField(primary_key=True)
    fromAccount = models.ForeignKey(Account, related_name='source_transactions', on_delete=models.CASCADE, null= True)
    toAccount = models.ForeignKey(Account, related_name='destination_transactions', on_delete=models.CASCADE, null= True)
    amount = models.DecimalField(max_digits=28, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)
    transactionType = models.CharField(max_length=6, choices=[('credit', 'Credit'), ('debit', 'Debit')], default = "Debit")
    
    def __str__(self):
        return f"Transaction ID: {self.TransactionID}"

    def save_transaction(self):
        self.save()

