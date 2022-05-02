from django.urls import path
from .views import bank_user_detail, bank_user_list

app_name = 'bankusers'

urlpatterns = [
    path('', bank_user_list, name='bank users'),
    path('<int:pk>/', bank_user_detail, name='bank detail')
]