from django.contrib import admin

# Register your models here.
from .models import Service,Booking,Product,Order

admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Product)
admin.site.register(Order)