from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from bankaccounts.models import BankAccount
from bankaccounts.rest_apis.serializers import BankAccountSerializer


@api_view(['GET', 'POST'])
def bank_account_list(request):

    if request.method == 'GET':
        accounts = BankAccount.objects.all()
        serializer = BankAccountSerializer(accounts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HHTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bank_account_detail(request, pk):
    try:
        account = BankAccount.objects.get(pk=pk)
    except BankAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer = BankAccountSerializer(account)
       return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BankAccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HHTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)