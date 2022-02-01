import email
from django.db import models
from django.forms import EmailField

# Create your models here.

class myUsers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(EmailField, max_length=50)
    password = models.CharField(max_length=20)