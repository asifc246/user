from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class user(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

