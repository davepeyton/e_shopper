from django.urls import path

from . import views

urlpatterns = [
  path('shop/', views.index) # my domain.com/shop
]