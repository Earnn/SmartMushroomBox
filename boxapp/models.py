from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea,TextInput,FileInput,ChoiceField
# Create your models here.

class Box(models.Model):
	"""docstring for Dog"""
	CHOICES = (
        ('Profile A', 'Profile A'),
        ('Profile B', 'Profile B'),
        ('Profile C', 'Profile C'),
        ('Profile D', 'Profile D'),

    )
	name = models.CharField(max_length=20,blank=True,null=True)
	code = models.CharField(max_length=20)
	password = models.CharField(max_length=20,blank=True)
	profile =models.CharField(max_length=100,blank=True,null=True,choices=CHOICES)
	temporature = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
	temporature_by_control = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
	humidity = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
	humidity_by_control = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
	color = models.CharField(max_length=20,blank=True,null=True)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	start_date = models.DateField(blank=True,null=True)
	end_date =models.DateField(blank=True,null=True)

class CreateBoxModelForm(ModelForm):
	class Meta:
		model = Box
		fields = [
			"code",
			"password",
		]
		widgets = {'code': TextInput(attrs={'placeholder': 'serial number','class':'uk-input'}),'password': TextInput(attrs={'placeholder': 'password','class':'uk-input'})}

class AddProfileBoxModelForm(ModelForm):
	class Meta:
		model = Box
		fields = [
			"name",
			"profile",
		]
		widgets = {
		'name': TextInput(attrs={'placeholder': 'name','class':'uk-input'}),

		}
