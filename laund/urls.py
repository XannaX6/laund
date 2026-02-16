from django.urls import path
from . import views

app_name = "laund"

urlpatterns = [
 path('', views.home, name='home'),
 path('shop/', views.shop, name='shop'),
 path('booking/', views.booking, name='booking'),
 path('pay/', views.pay, name='pay'),
]