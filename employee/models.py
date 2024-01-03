from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    phone=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=200)

class Employee(models.Model):
    name=models.CharField(max_length=100,unique=True)
   
    salary=models.PositiveIntegerField()
    department=models.CharField(max_length=150)
    


    def __str__(self):
        return self.name