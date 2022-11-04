from django.shortcuts import render
from core.models import Customer
from core.models import Item
from core.models import Order
from core.models import OrderItem

# Create your views here.
from core.serializers import CustomerSerializer
from core.serializers import ItemSerializer
from core.serializers import OrderSerializer
from core.serializers import OrderItemSerializer
from rest_framework import viewsets

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer