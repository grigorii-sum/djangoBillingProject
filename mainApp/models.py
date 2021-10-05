from django.db import models


class BankAccount(models.Model):
    name = models.CharField(max_length=100)
    is_overdraft = models.BooleanField()
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    donor_bank_account_id = models.ForeignKey(BankAccount, on_delete=models.SET_NULL, null=True, related_name='donor_bank_account_id')
    recipient_bank_account_id = models.ForeignKey(BankAccount, on_delete=models.SET_NULL, null=True, related_name='recipient_bank_account_id')
    amount = models.FloatField()
    is_sent = models.BooleanField()

    def __str__(self):
        return str(self.donor_bank_account_id) + ' TO ' + str(self.recipient_bank_account_id) + ' = ' + str(self.is_sent)
