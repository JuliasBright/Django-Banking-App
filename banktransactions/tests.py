from django.test import TestCase
from bankaccounts.models import BankAccount
from banktransactions.models import BankTransactions
from bankusers.models import Bankuser

# Create your tests here.

class modelTest(TestCase):
    def bank_transaction_test(self):
        bank_user = Bankuser.objects.create(user_name="Testinguser", user_surname="fromTheBanking" )
        bank_account = BankAccount.SavingAccount.object.create(user=bank_user, amount=50.00)
        bank_transaction = BankTransactions.transaction_action.value_from_object().Set(value ='transaction-action')
        bank_amount = BankTransactions.amount.object.create(amount=25.00)
        self.assertEqual(str(bank_user.user_name), "Testinguser", "bank user names are not equal")
        self.assertEqual(bank_account.amount, 50.00, "account amount not equal")
        self.assertEqual(bank_transaction.transaction_action,"transaction-action" "transaction action not equal")
        self.assertEqual(bank_account.amount, 25.00, "account amount not equal")
