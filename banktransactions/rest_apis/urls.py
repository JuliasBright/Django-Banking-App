from django.urls import path
from .views import bank_transaction_list, bank_transaction_detail

app_name = 'banktransactions'

urlpatterns = [
    path('', bank_transaction_list, name='bank transactions'),
    path('<int:pk>/', bank_transaction_detail, name='bank detail'),
]