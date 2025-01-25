from rest_framework import serializers
from .models import Product_model

class Product_serializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only =  True)
    class Meta:
        model = Product_model
        fields = [
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_my_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None