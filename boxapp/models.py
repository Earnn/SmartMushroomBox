from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea,TextInput,FileInput,ChoiceField,Select
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
	profile =models.CharField(max_length=100,null=True,choices=CHOICES,blank=False,default='Profile A')
	temporature = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
	temporature_by_control = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
	humidity = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
	humidity_by_control = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
	color_by_control = models.CharField(max_length=20,blank=True,null=True)
	status_color = models.CharField(max_length=20,blank=True,null=True)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	start_date = models.DateField(blank=True,null=True)
	end_date =models.DateField(blank=True,null=True)

class Buy(models.Model):
	name = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	order_amount = models.CharField(max_length=20)
		
class CreateBoxModelForm(ModelForm):
	class Meta:
		model = Box
		fields = [
			"code",
			#"password",
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
		'profile' : Select(attrs={'class':'uk-select','id':'profile'})
		}

class BuyBoxModelForm(ModelForm):
	class Meta:
		model = Buy
		fields = [
			"name",
			"email",
			"phone_number",
			"address",
			"order_amount",
		]
		widgets = {
		'name': TextInput(attrs={'placeholder': 'ชื่อ-นามสกุล','class':'uk-input','id':'form-stacked-text','type':"text"}),
		'address' : TextInput(attrs={'placeholder': 'ที่อยู่','class':'uk-input','id':'form-stacked-text','type':"text"}),
		'phone_number' : TextInput(attrs={'placeholder': 'เบอร์โทร','class':'uk-input','id':'form-stacked-text','type':"text"}),
		'email': TextInput(attrs={'placeholder': 'Email','class':'uk-input','id':'form-stacked-text','type':"email"}),
		'order_amount' : TextInput(attrs={'placeholder': 'จำนวนสั่งซื้อ','class':'uk-input','id':'form-stacked-text','type':"number",'min':"1"}),
	
		}
