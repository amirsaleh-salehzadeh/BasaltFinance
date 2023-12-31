# Generated by Django 4.2.5 on 2023-09-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0004_alter_account_balance'),
        ('transactionApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='TransactionID',
            new_name='transactionId',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='AccountID',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='TransactionType',
        ),
        migrations.AddField(
            model_name='transaction',
            name='fromAccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_transactions', to='accountApp.account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='toAccount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_transactions', to='accountApp.account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactionType',
            field=models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], default='Debit', max_length=6),
        ),
    ]
