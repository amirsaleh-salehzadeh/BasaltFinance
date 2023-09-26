from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Transaction
from transactionApp.serializer import TransactionSerializer
from accountApp.models import Account
from rest_framework.decorators import action
from _decimal import Decimal
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required

@swagger_auto_schema(
    request_body=TransactionSerializer, 
    responses={status.HTTP_201_CREATED: TransactionSerializer()}, 
    operation_description="Create a new transaction",
    operation_summary="Create Transaction",
    manual_parameters=[
        openapi.Parameter(
            name='fromAccount',
            in_=openapi.IN_FORM,
            type=openapi.TYPE_INTEGER,
            description="ID of the source account",
            required=True,
        ),
        openapi.Parameter(
            name='toAccount',
            in_=openapi.IN_FORM,
            type=openapi.TYPE_INTEGER,
            description="ID of the destination account",
            required=True,
        ),
        openapi.Parameter(
            name='amount',
            in_=openapi.IN_FORM,
            type=openapi.TYPE_NUMBER,
            description="Transaction amount",
            required=True,
        ),
        openapi.Parameter(
            name='transactionType',
            in_=openapi.IN_FORM,
            type=openapi.TYPE_STRING,
            enum=["credit", "debit"],  
            description="Type of transaction (credit or debit)",
            required=True,
        ),
    ],
)
@action(detail=False, methods=['post'])
@login_required
def create_transaction(request):
    """
    API endpoint that allows transactions to be viewed or created.
    
    Create a new transaction.
    
    Parameters:
    - fromAccount (int): ID of the source account.
    - toAccount (int): ID of the destination account.
    - amount (decimal): Transaction amount.
    - transactionType (str): Type of transaction (credit or debit).
    
    Returns:
    - transaction (object): Created transaction object.
    """
    try:
        fromAccount_id = request.POST['fromAccount']
        toAccount_id = request.POST['toAccount']
        amount = request.POST['amount']
        transaction_type = request.POST['transactionType']

        fromAccount = Account.objects.get(accountid=fromAccount_id)
        toAccount = Account.objects.get(accountid=toAccount_id)

        transaction = Transaction(
            fromAccount=fromAccount,
            toAccount=toAccount,
            amount=amount,
            transactionType=transaction_type
        )
        transaction.save()
        if transaction_type == 'credit':
            fromAccount.debit(Decimal(amount))
            toAccount.credit(Decimal(amount))
        else:
            toAccount.debit(Decimal(amount))
            fromAccount.credit(Decimal(amount))

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)