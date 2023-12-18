from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    customer_id = models.CharField(max_length=50, primary_key = True)
    
    
    
    
class Order(models.Model):
    order_name = models.CharField(max_length=50)
    order_date = models.DateField(auto_now_add = True)
    order_time = models.TimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)