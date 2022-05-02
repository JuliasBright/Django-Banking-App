from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from banktransactions.models import BankTransactions
from banktransactions.rest_apis.serializers import BankTransactionsSerializer


@api_view(['GET', 'POST'])
def bank_transaction_list(request):

    if request.method == 'GET':
        transaction = BankTransactions.objects.all()
        serializer = BankTransactionsSerializer(transaction, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BankTransactionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HHTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bank_transaction_detail(request, pk):
    try:
        transaction = BankTransactions.objects.get(pk=pk)
    except BankTransactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer = BankTransactionsSerializer(transaction)
       return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BankTransactionsSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HHTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



