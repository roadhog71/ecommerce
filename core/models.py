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
