from django.db import models
class login():
    firstname=models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30, blank=True)

# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed

# Create your models here.
class Contact(models.Model):
    # sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # phone = models.CharField(max_length=10)
    message = models.CharField(max_length=300)


