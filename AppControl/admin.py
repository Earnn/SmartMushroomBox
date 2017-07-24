from django.contrib import admin
from .models import Box,Profile
# Register your models here.
class BoxAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Box._meta.fields]
	list_editable=("temp","humi")
admin.site.register(Box,BoxAdmin)

class ProgramAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Profile._meta.fields]
admin.site.register(Profile,ProgramAdmin)