from email.policy import default
from msilib.schema import Class
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Customer(models.Model):
    id= models.BigAutoField(primary_key= True)
    first_name= models.CharField(max_length= 64)
    last_name= models.CharField(max_length= 64)

    class Meta:
        db_table = 'customers'
        managed= True
         
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Item(models.Model):
    id= models.BigAutoField(primary_key= True)
    item= models.CharField(max_length= 64)
    price= models.PositiveIntegerField()

    class Meta:
        db_table = 'items'
        managed= True
         
    def __str__(self) -> str:
        return f"{self.item} ${self.price}"

class Order(models.Model):
    id= models.BigAutoField(primary_key= True)
    date= models.DateField()
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    status= models.SmallIntegerField(default=1)

    class Meta:
        db_table = 'orders'
        managed= True
         
    def __str__(self) -> str:
        return f"{self.date} {self.customer} {self.status}"

class OrderItem(models.Model):
    id= models.BigAutoField(primary_key= True)
    order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name = 'order_items')
    item= models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity= models.DecimalField(max_digits = 6, decimal_places = 2)
    price= models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        db_table = 'order_items'
        managed= True
         
    def __str__(self) -> str:
        return f"{self.item} {self.quantity} {self.price}"
