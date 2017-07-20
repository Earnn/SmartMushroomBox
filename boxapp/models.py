from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Box(models.Model):
  code = models.CharField(max_length=20)
  password = models.CharField(max_length=20,blank=True)
  temporature = models.DecimalField(max_digits=15, decimal_places=2)
  temporature_by_control = models.DecimalField(max_digits=15, decimal_places=2)
  humidity = models.DecimalField(max_digits=15, decimal_places=2)
  humidity_by_control = models.DecimalField(max_digits=15, decimal_places=2)
  color = models.CharField(max_length=20)
  owner = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
  
