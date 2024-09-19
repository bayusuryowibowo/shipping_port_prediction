from django.contrib import admin

# Register your models here.
from .models.shipping_port import ShippingPort

admin.site.register(ShippingPort)