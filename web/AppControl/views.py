from django.shortcuts import render
from django.http import HttpResponse
from .models import Box,Profile,Sn
from .forms import ProfileForm
from django.shortcuts import redirect
from django.core import serializers
from django.db.models import Min, Max
import json
import random
from boxapp.models import Box
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Box2
# Create your views here.

def getdata(request,nodeid,temp,humi,key):
    intit_program = Box.objects.all().filter(code=nodeid).values('profile')
    program = intit_program[0]['profile'].split()[1]
    # day = 3
    # Box2.objects.get(code__code=nodeid)
    res =  Box2.objects.filter(code__code=nodeid).values('time').aggregate(old=Min('time'), new=Max('time'))
    old, new = res['old'], res['new']
    day = (new - old).days
    print (day)
    #help(day)
    t,h,o,t2,h2,r,g,b = getprogram(program,day)
    command = "%03d,%03d,%03d,%03d,%03d,%03d,%03d,%03d"%(t,h,o,t2,h2,r,g,b)
    if key=="2345678909876543234567898765":
        data_box = Box2(code = Box.objects.get(
            code=nodeid) , 
            temp= float(temp),  
            humi = float(humi),
        )
        data_box.save()
        data_box_update = Box.objects.update_or_create(
            code            = nodeid,
            defaults        = {
                'temporature' : temp,
                'humidity'  : humi,
            }
        )
        print ("Save")
    else:
        print ("UnSave")
    return HttpResponse(command,content_type='text/plain')

def getprogram(program,day):
    y = program
    x = day
    data = Profile.objects.all().filter(day=x,name=y).values('day','temp','humi','ontime','temp_closelight','humi_closelight','lred','lgreen','lblue')
    #print(data[0]['temp'])
    t = data[0]['temp']
    h = data[0]['humi']
    o = data[0]['ontime']
    t2 = data[0]['temp_closelight']
    h2 = data[0]['humi_closelight']
    r = data[0]['lred']
    g = data[0]['lgreen']
    b = data[0]['lblue']
    command = (t,h,o,t2,h2,r,g,b)
    print(command)
    return command

@staff_member_required
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
