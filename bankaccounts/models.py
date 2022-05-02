from django.db import models
from bankusers.models import Bankuser

# Create your models here.
class BankAccount(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    users = models.ForeignKey(Bankuser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def SavingAccount(self):
        id = models.ForeignKey(BankAccount.id)
        users = models.ForeignKey(BankAccount.users)
        amount = models.DecimalField(default=0, max_digits=4, decimal_places=2)
        

    def CreditAccount(self):
        id = models.ForeignKey(BankAccount.id)
        users = models.ForeignKey(BankAccount.users)
        amount = models.DecimalField(default=0, max_digits=7, decimal_places=2)

 


    def __str__(self):
        return str(self.id)
    

  

