from rest_framework import serializers
from banktransactions.models import BankTransactions



class BankTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransactions
        fields = '__all__'