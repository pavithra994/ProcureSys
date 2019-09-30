from django.contrib import admin
from order.models import Order,Tender,Invoice

# Register your models here.
admin.site.register(Order)
admin.site.register(Tender)
admin.site.register(Invoice)