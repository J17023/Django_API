from rest_framework import serializers
from .models import Product_model_version_one
from django.contrib.auth import get_user_model

User = get_user_model()     

class Product_serializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only =  True)
    class Meta:
        model = Product_model_version_one
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
   

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk',
        read_only = True
    )
    name = serializers.CharField(read_only = True)

class User_public_serializer(serializers.Serializer):
    username = serializers.CharField(read_only =True)
    this_is_not_real = serializers.CharField(read_only = True)
    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = User
        fields = [
            'username',
            'this_is_not_real',
            'id'
        ]
    # other_products = serializers.SerializerMethodField(read_only =True)

    # def get_other_products(self,obj):
    #     user = obj
    #     my_products_qs = user.products.all()[:5]
    #     return UserProductInlineSerializer(my_products_qs, many = True, 
    #                                        context = self.context).data

