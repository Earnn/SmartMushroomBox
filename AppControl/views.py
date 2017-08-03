from django.shortcuts import render
from django.http import HttpResponse
from .models import Box,Profile,Sn
from .forms import ProfileForm
from django.shortcuts import redirect
from django.core import serializers
import json
import random
from boxapp.models import Box
# Create your views here.

def getdata(request,nodeid,temp,humi,key):
	#node = request.POST['nodeid']
	temp = "20"
	humi = "80"
	ontime = "14"
	lred = "999"
	lgreen = "999"
	lblue = "999"
	command = "%s,%s,%s,%s,%s,%s"%(temp,humi,ontime,lred,lgreen,lblue)
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
def addprogram(request):
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
			name=name,
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
	y = "A"
	x = 3
	data = Profile.objects.all().filter(day=x,name=y).values('day','temp','humi','ontime','lred','lgreen','lblue')
	#print(data[0]['temp'])
	t = data[0]['temp']
	h = data[0]['humi']
	o = data[0]['ontime']
	r = data[0]['lred']
	g = data[0]['lgreen']
	b = data[0]['lblue']
	command = "%03d,%03d,%03d,%03d,%03d,%03d"%(t,h,o,r,g,b)
	print(command)
	return HttpResponse(command)
def genSN(request):
	x = random.randint(1,10000000000)
	y=("%010d"%x)
	print(y)
	sn = Box.objects.create(
		code=y,
		)
	sn.save()
	print("S/N Save")
	#return HttpResponse(x)
	return render(request, 'sn.html', {'sn':y})
