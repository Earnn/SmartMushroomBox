from django.contrib import admin
from .models import Box2,Profile,Sn
# Register your models here.
class Box2Admin(admin.ModelAdmin):
	list_display=[f.name for f in Box2._meta.fields]
	list_editable=("temp","humi")
	list_filter=['code']
admin.site.register(Box2,Box2Admin)

class ProgramAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Profile._meta.fields]
	list_editable=("day","temp","humi","ontime","temp_closelight","humi_closelight","lred","lgreen","lblue")
	list_filter=['name']
admin.site.register(Profile,ProgramAdmin)
