from django.db import models
from userApp.models import User

class Account(models.Model):
    accountid = models.AutoField(primary_key=True)  # Using AutoField as the primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=28, decimal_places=4, default=0)
    account_name = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return f"Account {self.accountid} for {self.user.username}"

    def credit(self, amount):
        """
        Credit the account with a specified amount.

        Args:
            amount (Decimal): The amount to be credited to the account.
        """
        self.balance += amount
        self.save()

    def debit(self, amount):
        """
        Debit the account by a specified amount.

        Args:
            amount (Decimal): The amount to be debited from the account.

        Raises:
            ValueError: If the amount is greater than the account balance.
        """
        if amount <= self.balance:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("Insufficient balance")

    def get_balance(self):
        """
        Get the current balance of the account.

        Returns:
            Decimal: The current balance of the account.
        """
        return self.balance