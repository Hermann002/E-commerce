from django.urls import path
from shop.views import index, detail, checkout

urlpatterns = [
    path('', index, name='home'),
    path('<int:pk>/', detail, name='detail'),
    path('checkout/', checkout, name='checkout')
]
