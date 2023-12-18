from django.urls import path
from .views import *


urlpatterns = [
    path('customer', CustomerList.as_view()),
    path('customer/<path:pk>', CustomerDetails.as_view()),
    path('order', OrderList.as_view()),
    path('order/<path:pk>', OrderDetails.as_view()),
]
