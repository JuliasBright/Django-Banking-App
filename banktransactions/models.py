from django.db import models
from bankaccounts.models import BankAccount
from bankusers.models import Bankuser


# Create your models here.
class BankTransactions(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    account = models.ForeignKey(BankAccount, on_delete=models.SET_NULL, default=None, null=True)
    users = models.ForeignKey(Bankuser, on_delete=models.SET_NULL, default=None, null=True)
    transaction_action = models.CharField(max_length=100)
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self): 
        return str(self.id)

       