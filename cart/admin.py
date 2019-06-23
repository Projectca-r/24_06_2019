from django.contrib import admin
from .models import *

# class CartAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Cart

# Register your models here.
# admin.site.register(Cart, CartAdmin)
admin.site.register(Cart)