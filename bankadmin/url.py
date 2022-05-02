from . import views
from django.shortcuts import render
from django.urls import path

app_name = 'bankadmin'

urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
  
]

