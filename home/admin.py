from django.contrib import admin
from home.models import  CartItem, Contact, Order, Product
# Register your models here.

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)