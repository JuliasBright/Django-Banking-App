from django.shortcuts import render
import csv
from django.shortcuts import render
from django.http import HttpResponse
from bankusers.models import Bankuser
from banktransactions.models import BankTransactions
from bankaccounts.models import BankAccount 
from banktransactions.models import BankTransactions


def index(request, pk):
    headerAccount = ['ID', 'USER ID', 'TYPE', 'AMOUNT']
    headerTransaction = ['ID', 'USER ID', 'ACTION', 'AMOUNT']
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=report.csv'
    print(pk)
    user = Bankuser.objects.get(id=pk)
    accounts = BankAccount.objects.filter(user=user.id)
    
    writer = csv.writer(response)
    writer.writerow(headerAccount)

    for account in accounts:
        writer.writerow([account.id, account.user, account.amount])
    
    transactions = BankTransactions.objects.filter(user=user)
    writer.writerow([])

    writer.writerow(headerTransaction)

    for transaction in transactions:
        writer.writerow([transaction.id, transaction.user, transaction.action, transaction.amount])

    return response
