from django.urls import path
from .views import bank_account_list, bank_account_detail

app_name = 'bankaccounts'

urlpatterns = [
    path('', bank_account_list, name='bank accounts'),
    path('<int:pk>/', bank_account_detail, name='bank details')
]