from django.contrib import admin
from .models import Category, Product, Profile, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
