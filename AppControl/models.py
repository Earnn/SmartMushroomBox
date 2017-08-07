from django.db import models
from django.utils import timezone
from boxapp.models import Box
from django.forms import ModelForm, Textarea,TextInput,FileInput,ChoiceField,Select
# Create your models here.
class Box2(models.Model):
    time    = models.DateTimeField(auto_now_add=True)
    code    = models.ForeignKey(Box, on_delete=models.SET_NULL,blank=True,null=True)
    temp    = models.FloatField(default=0.0)
    humi    = models.FloatField(default=0.0)

    # def __unicode__(self):
    #     return 'adwdwaf'
    #class Meta:
     #   ordering = ['nodeid']
class Profile(models.Model):
    name    = models.CharField(max_length=20,default=0)
    day     = models.IntegerField(max_length=3,blank=False,default=0.0)
    temp    = models.FloatField(default=0.0)
    humi    = models.FloatField(default=0.0)
    ontime  = models.IntegerField(default=0)
    temp_closelight = models.FloatField(default=0.0)
    humi_closelight = models.FloatField(default=0)
    lred    = models.IntegerField(default=0)
    lgreen  = models.IntegerField(default=0)
    lblue   = models.IntegerField(default=0)
    class Meta:
        ordering = ['name']

class Sn(models.Model):
    sn = models.CharField(default=0,blank=False,max_length=10)


class UpdateProfileBoxModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "day",
            "temp",
            "humi",
            "ontime",
            "lred",
            "lgreen",
            "lblue"
        ]
        widgets = {
        'name': TextInput(attrs={'placeholder': 'ชื่อ-นามสกุล','class':'uk-input','id':'form-stacked-text','type':"text"}),
        'day' : TextInput(attrs={'placeholder': '','class':'uk-input','id':'form-stacked-text','type':"number",'min':"1"}),
        'temp' : TextInput(attrs={'placeholder': '','class':'uk-input','id':'form-stacked-text','type':"number",'min':"1"}),
        'humi' : TextInput(attrs={'placeholder': '','class':'uk-input','id':'form-stacked-text','type':"number",'min':"1"}),
        'ontime' : TextInput(attrs={'placeholder': '','class':'uk-input','id':'form-stacked-text','type':"number",'min':"1"}),
        'lred' : TextInput(attrs={'placeholder': '','class':'uk-input','id':'form-stacked-text','type':"number",'min':"1"}),
        'lgreen' : TextInput(attrs={'placeholder': '','class':'uk-input','id':'form-stacked-text','type':"number",'min':"1"}),
        'lblue' : TextInput(attrs={'placeholder': '','class':'uk-input','id':'form-stacked-text','type':"number",'min':"1"}),

    
        }