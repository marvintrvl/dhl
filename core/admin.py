from django.contrib import admin
from .models import Customer, Business, Package, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Business)
admin.site.register(Package)
admin.site.register(Order)