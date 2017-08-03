from django.db import models
from django.utils import timezone
# Create your models here.
class Box(models.Model):
    time    = models.DateTimeField(auto_now_add=True)
    nodeid  = models.CharField(max_length=10, blank=False)
    temp    = models.FloatField(default=0.0)
    humi    = models.FloatField(default=0.0)
    class Meta:
        ordering = ['nodeid']
class Profile(models.Model):
    name    = models.CharField(max_length=20,default=0)
    day     = models.CharField(max_length=3,blank=False,default=0.0)
    temp    = models.IntegerField(default=0.0)
    humi    = models.IntegerField(default=0.0)
    ontime  = models.IntegerField(default=0)
    lred    = models.IntegerField(default=0)
    lgreen  = models.IntegerField(default=0)
    lblue   = models.IntegerField(default=0)

class Sn(models.Model):
    sn = models.CharField(default=0,blank=False,max_length=10)
    