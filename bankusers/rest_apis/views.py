from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from bankusers.models import Bankuser
from bankusers.rest_apis.serializers import BankUserSerializer


@api_view(['GET', 'POST'])
def bank_user_list(request):

    if request.method == 'GET':
        users = Bankuser.objects.all()
        serializer = BankUserSerializer(users, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BankUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HHTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bank_user_detail(request, pk):
    try:
        user = Bankuser.objects.get(pk=pk)
    except Bankuser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer = BankUserSerializer(user)
       return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BankUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HHTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)