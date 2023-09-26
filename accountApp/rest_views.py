from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from accountApp.models import Account
from _decimal import Decimal
from accountApp.serializer import AccountSerializer

@swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'amount': openapi.Schema(
                type=openapi.TYPE_NUMBER,
                description='Amount to credit to the account'
            )
        },
        required=['amount']
    ),
    responses={
        200: 'Account credited successfully',
        400: 'Bad Request',
        404: 'Account not found'
    },
    operation_summary='Credit of a Specific Account',
    operation_description='Credit a specific account belonging to the authenticated user.'
)
@login_required
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def credit_account(request, account_id):
    try:
        # Check if the account belongs to the authenticated user
        account = Account.objects.get(user=request.user, accountid=account_id)
        amount = request.data.get('amount')

        # Ensure 'amount' is a positive number
        if amount <= 0:
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

        account.credit(amount)
        return Response({'message': 'Account credited successfully'}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)  
    
    
@swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'amount': openapi.Schema(
                type=openapi.TYPE_NUMBER,
                description='Amount to debit from the account'
            )
        },
        required=['amount']
    ),
    responses={
        200: 'Account debited successfully',
        400: 'Bad Request',
        404: 'Account not found'
    },
    operation_summary='Debit of a Specific Account',
    operation_description='Debit a specific account belonging to the authenticated user.'
)   
@login_required
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def debit_account(request, account_id):
    try:
        # Check if the account belongs to the authenticated user
        account = Account.objects.get(user=request.user, accountid=account_id)
        amount = request.data.get('amount')

        # Ensure 'amount' is a positive number
        if amount <= 0:
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

        account.debit(amount)
        return Response({'message': 'Account debited successfully'}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    responses={
        200: openapi.Response(
            description='Successful response',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'balance': openapi.Schema(
                        type=openapi.TYPE_NUMBER,
                        description='Current account balance'
                    )
                }
            )
        ),
        404: 'Account not found'
    },
    operation_summary='Balance of a Specific Account',
    operation_description='Retrieve the balance of a specific account belonging to the authenticated user.'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@login_required
def balance_of_account(request, account_id):
    try:
        account = Account.objects.get(user=request.user, accountid=account_id)
        balance = account.get_balance()
        return Response({'balance': balance}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
