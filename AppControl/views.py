from django.shortcuts import render
from django.http import HttpResponse
from .models import Box,Profile,Sn
from .forms import ProfileForm
from django.shortcuts import redirect
from django.core import serializers
import json
import random
# Create your views here.

def getdata(request,nodeid,temp,humi,key):
	#node = request.POST['nodeid']
	c_temp = "100"
	c_humi = "200"
	if float(temp) >= 20:
		c_temp = "101"
	if float(temp) <= 16:
		c_temp = "100"
	if float(humi) <= 40:
		c_humi = "201"
	if float(humi) >= 80:
		c_humi = "200"
	command = "%s,%s"%(c_temp,c_humi)
	if key=="2345678909876543234567898765":
		data_box = Box(
			nodeid = nodeid ,
			temp 	= float(temp), 
			humi 	= float(humi),
			)
		data_box.save()
		print ("Save")
	else:
		print ("UnSave")
	return HttpResponse(command,content_type='text/plain')
def addprofile(request):
	#form = None
	#if request.method == 'POST':
	form = ProfileForm(request.POST or None)
	if form.is_valid():
		day = request.POST['day']
		temp = request.POST['temp']
		humi = request.POST['humi']
		ontime = request.POST['ontime']
		lred = request.POST['lred']
		lgreen = request.POST['lgreen']
		lblue = request.POST['lblue']
		post = Profile.objects.create(
			day=day,
			temp=temp,
			humi=humi,
			ontime=ontime,
			lred=lred,
			lgreen=lgreen,
			lblue=lblue,
		)
		post.save()
		return redirect('addprogram')  
	else:
		form = ProfileForm()
	return render(request, 'addprofile.html', {'form': form})
	#return render(request, 'addprofile.html')

def getprogram(request):
	data = Profile.objects.all().values('day','temp','humi','ontime','lred','lgreen','lblue')[:1:1]
	print(data)
	return HttpResponse(data)
def genSN(request):
	x = random.randint(1,10000000000)
	y=("%010d"%x)
	print(y)
	sn = Sn.objects.create(
		sn=y,
		)
	sn.save()
	print("S/N Save")
	#return HttpResponse(x)
	return render(request, 'sn.html', {'sn':y})
