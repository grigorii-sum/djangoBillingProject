from django.urls import path

from .views import bank_account_create_endpoint, transaction_create_endpoint, get_bank_account_balance_endpoint

urlpatterns = [
    path('bank-account/create/', bank_account_create_endpoint, name="bank-account-create"),
    path('transaction/create/', transaction_create_endpoint, name="transaction-create"),
    path('bank-account/balance/<int:pk>/', get_bank_account_balance_endpoint, name="get-bank-account-balance"),
]