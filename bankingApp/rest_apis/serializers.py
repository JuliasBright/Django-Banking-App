from rest_framework import serializers
from bankusers.models import Bankuser

class BankingAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankuser
        fields = '__all__'