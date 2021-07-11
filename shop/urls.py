from django.urls import path
from django.http import HttpResponce

urlpatterns = [
    path('shop/', views.index)
]