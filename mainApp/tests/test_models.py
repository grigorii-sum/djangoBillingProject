from django.test import TestCase
from mainApp.models import BankAccount, Transaction


class BankAccountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        BankAccount.objects.create(name='testBankAccount', is_overdraft=False)

    def test_name_field(self):
        bank_account = BankAccount.objects.get(id=1)
        name_of_bank_account = bank_account.name

        self.assertEquals(name_of_bank_account, 'testBankAccount')

    def test_is_overdraft_field(self):
        bank_account = BankAccount.objects.get(id=1)
        flag_of_bank_account = bank_account.is_overdraft

        self.assertEquals(flag_of_bank_account, False)

    def test_balance_field(self):
        bank_account = BankAccount.objects.get(id=1)
        balance_of_bank_account = bank_account.balance

        self.assertEquals(balance_of_bank_account, 0.0)

    def test_user_id_max_length(self):
        bank_account = BankAccount.objects.get(id=1)
        max_length = bank_account._meta.get_field('name').max_length

        self.assertEquals(max_length, 100)


class TransactionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        first_account = BankAccount.objects.create(name='testBankAccount1', is_overdraft=False)
        second_account = BankAccount.objects.create(name='testBankAccount2', is_overdraft=False)
        Transaction.objects.create(donor_bank_account_id=first_account, recipient_bank_account_id=second_account, amount=100.0, is_sent=False)

    def test_donor_bank_account_id_field(self):
        transaction = Transaction.objects.get(id=1)
        donor_bank_account_id = transaction.donor_bank_account_id.id

        self.assertEquals(donor_bank_account_id, 1)

    def test_recipient_bank_account_id_field(self):
        transaction = Transaction.objects.get(id=1)
        recipient_bank_account_id = transaction.recipient_bank_account_id.id

        self.assertEquals(recipient_bank_account_id, 2)

    def test_amount_field(self):
        transaction = Transaction.objects.get(id=1)
        amount = transaction.amount

        self.assertEquals(amount, 100.0)

    def test_is_sent_field(self):
        transaction = Transaction.objects.get(id=1)
        is_sent = transaction.is_sent

        self.assertEquals(is_sent, False)
