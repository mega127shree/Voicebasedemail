from django.db import models

class UserDetails(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    name=models.CharField(max_length=50)

class LoginDetails(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)

class option(models.Model):
    option = models.CharField(max_length=100)

class Compose:
    recipient : str
    subject : str
    body : str
    
class Topic(models.Model):
           id = models.AutoField(primary_key=True)