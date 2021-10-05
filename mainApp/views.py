from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import BankAccount, Transaction
from .serializers import BankAccountSerializer, TransactionSerializer


@api_view(['POST'])
def bank_account_create_endpoint(request):
    serializer = BankAccountSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def transaction_create_endpoint(request):
    serializer = TransactionSerializer(data=request.data)

    if serializer.is_valid():
        donor_bank_account_id = request.data["donor_bank_account_id"]
        recipient_bank_account_id = request.data["recipient_bank_account_id"]
        amount = float(request.data["amount"])
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    donor_bank_account = BankAccount.objects.get(pk=donor_bank_account_id)
    recipient_bank_account = BankAccount.objects.get(pk=recipient_bank_account_id)

    if donor_bank_account.is_overdraft or ((donor_bank_account.balance - amount) >= 0):
        donor_bank_account.balance -= amount
        donor_bank_account.save()
        recipient_bank_account.balance += amount
        recipient_bank_account.save()

        new_transaction = Transaction.objects.create(
            donor_bank_account_id=donor_bank_account,
            recipient_bank_account_id=recipient_bank_account,
            amount=amount,
            is_sent=True
        )
        new_transaction.save()
    else:
        new_transaction = Transaction.objects.create(
            donor_bank_account_id=donor_bank_account,
            recipient_bank_account_id=recipient_bank_account,
            amount=amount,
            is_sent=False
        )
        new_transaction.save()

        Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    content = {
        "is_sent": new_transaction.is_sent
    }
    return Response(content, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_bank_account_balance_endpoint(request, pk):
    try:
        bank_account = BankAccount.objects.get(pk=pk)
    except:
        content = {
            "error": "Bank account with requested PK was not found"
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    serializer = BankAccountSerializer(bank_account)
    content = {
        "balance": serializer.data["balance"]
    }
    return Response(content, status=status.HTTP_200_OK)
