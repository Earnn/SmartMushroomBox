from django.contrib import admin
from .models import *

class BoxAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Box._meta.fields]
admin.site.register(Box, BoxAdmin)

class BuyAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Buy._meta.fields]
admin.site.register(Buy, BuyAdmin)

class PaymentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Document2._meta.fields]
admin.site.register(Document2, PaymentAdmin)
