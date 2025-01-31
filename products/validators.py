from .models import Product_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

def validate_name(value):
    qs = Product_model.objects.filter(name__iexact = value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name")
    return value

def validate_name_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f'Hello is not allowed')
    return value

unique_product_title = UniqueValidator(queryset= Product_model.objects.all())