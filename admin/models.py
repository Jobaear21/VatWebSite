from django.db import models
from django.urls import reverse  
from django.contrib.auth.models import User

class User(models.Model):
   fname = models.CharField(max_length=200)
   fname = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   textarea = models.CharField(max_length=200)
   def __unicode__(self):  
     return self.fname
