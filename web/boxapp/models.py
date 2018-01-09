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
	code = models.CharField(max_length=20,unique=True)
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

	def __str__(self):
		return self.code

class Buy(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=20)   ##Edit CharField to EmailField
	phone_number = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	order_amount = models.CharField(max_length=20)
class BuyM(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=20)   ##Edit CharField to EmailField
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
class BuyMushroomModelForm(ModelForm):
	class Meta:
		model = BuyM
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
		
class Document2(models.Model):
    name = models.CharField(max_length=255, blank=True)
    amount = models.CharField(max_length=255,blank=False)
    timeTransfer = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255, blank=True)
    document    = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

#class Document(models.Model):
#    description = models.CharField(max_length=255, blank=True)
#    document    = models.FileField(upload_to='documents/')
#    uploaded_at = models.DateTimeField(auto_now_add=True)