from django.contrib import admin

# Register your models here.
from .models import Product_model

admin.site.register(Product_model)