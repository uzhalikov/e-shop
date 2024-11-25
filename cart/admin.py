from django.contrib import admin
from .models import CartItem, CartUser

admin.site.register(CartItem)
admin.site.register(CartUser)