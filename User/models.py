from django.db import models
from django.urls import reverse  
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
   fname = models.CharField(max_length=20)
   lname = models.CharField(max_length=20)
   email = models.CharField(max_length=200)
   phone = models.IntegerField(max_length=20)
   textarea = models.CharField(max_length=500)
   def __unicode__(self):
     return self.fname