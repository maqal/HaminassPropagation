from django.http import Http404
from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .appSerializer import *
from rest_framework.views import APIView


# Create your views here.
class CustomerList(APIView):
    # list all customers
    def get(self, reques, format = None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many = True)
        return Response(serializer.data)
    
    # add new customer
    def post(self, request, format = None):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CustomerDetails(APIView):
        # get by id
        def get_object(self, pk):
            try:
                return Customer.objects.get(pk = pk)
            except:
                raise Http404
            
        def get(self, request, pk, format = None):
            customer = self.get_object(pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        
        def put(self, request, pk, format = None):
            customer = self.get_object(pk)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk, format = None):
            customer = self.get_object(pk)
            customer.delete()
            return Response('Item deleted', status=status.HTTP_204_NO_CONTENT)
        
class OrderList(APIView):
    # list all customers
    def get(self, reques, format = None):
        customers = Order.objects.all()
        serializer = OrderSerializer(customers, many = True)
        return Response(serializer.data)
    
    # add new customer
    def post(self, request, format = None):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderDetails(APIView):
        # get by id
        def get_object(self, pk):
            try:
                return Order.objects.get(pk = pk)
            except:
                raise Http404
            
        def get(self, request, pk, format = None):
            order = self.get_object(pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        
        def put(self, request, pk, format = None):
            order = self.get_object(pk)
            serializer = CustomerSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk, format = None):
            order = self.get_object(pk)
            order.delete()
            return Response('Item deleted', status=status.HTTP_204_NO_CONTENT)
        