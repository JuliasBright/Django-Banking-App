from unicodedata import name
from django.test import TestCase
from .models import BankAccount
from bankusers.models import Bankuser

# Create your tests here.

class ModelTests(TestCase):
    def Account(self):
        Bankuser.objects.create(user_name = "Julius", user_surname = "Bright")

    def Saving_Account(self):
        user = Bankuser.objects.get(user_name="Julius")
        account = BankAccount.SavingAccount.objects.create(user=user, amount=50.00)
        self.assertEqual(account.amount, 50.00, "account amount not equal")
        self.assertEqual(account.user, user, "account user does not exist")

    def Credit_Account(self):
        user = Bankuser.objects.get(name="Julius")
        account = BankAccount.CreditAccount.objects.create(user=user, amount=20000.00)
        self.assertEqual(account.amount, 20000.00, "account amount is not equal")
        self.assertEqual(account.user, user, "account user does not exist")
