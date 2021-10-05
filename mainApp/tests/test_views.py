from django.test import Client, TestCase

from mainApp.models import BankAccount


class CreatingBankAccountViewTest(TestCase):

    def test_successful_creating_bank_account_endpoint(self):
        client = Client()
        context = {
            'name': 'testBankAccount10',
            'is_overdraft': 'True'
        }
        resp = client.post('/billing/bank-account/create/', context)

        self.assertEqual(resp.status_code, 201)

    def test_wrong_creating_bank_account_endpoint(self):
        client = Client()
        context = {
            'name': 'testBankAccount10',
            'is_overdraft': 10
        }
        resp = client.post('/billing/bank-account/create/', context)

        self.assertEqual(resp.status_code, 400)


class CreatingTransactionViewTest(TestCase):

    def test_successful_creating_transaction_endpoint(self):
        client = Client()
        first_account = BankAccount.objects.create(name='testBankAccount1', is_overdraft=False)
        second_account = BankAccount.objects.create(name='testBankAccount2', is_overdraft=False)
        context = {
            'donor_bank_account_id': first_account.id,
            'recipient_bank_account_id': second_account.id,
            'amount': 15.0
        }
        resp = client.post('/billing/transaction/create/', context)

        self.assertEqual(resp.status_code, 201)

    def test_wrong_creating_transaction_endpoint(self):
        client = Client()
        first_account = BankAccount.objects.create(name='testBankAccount1', is_overdraft=False)
        second_account = BankAccount.objects.create(name='testBankAccount2', is_overdraft=False)
        context = {
            'donor_bank_account_id': first_account.id,
            'recipient_bank_account_id': second_account.id,
            'amount': True
        }
        resp = client.post('/billing/transaction/create/', context)

        self.assertEqual(resp.status_code, 400)


class GettingBankAccountBalanceViewTest(TestCase):

    def test_successful_getting_bank_account_balance_endpoint(self):
        client = Client()
        BankAccount.objects.create(name='testBankAccount1', is_overdraft=False)
        resp = client.get('/billing/bank-account/balance/1/')

        self.assertEqual(resp.status_code, 200)

    def test_wrong_getting_bank_account_balance_endpoint(self):
        client = Client()
        resp = client.get('/billing/bank-account/balance/1/')

        self.assertEqual(resp.status_code, 400)
