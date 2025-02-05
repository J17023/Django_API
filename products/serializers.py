from rest_framework import serializers
from .models import Product_model
from rest_framework.reverse import reverse
from main_api.serializers import User_public_serializer
from . import validators

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk',
        read_only = True
    )
    name = serializers.CharField(read_only = True)

class Product_serializer(serializers.ModelSerializer):
    owner = User_public_serializer(source = "user", read_only =True)
    edit_url = serializers.SerializerMethodField(read_only= True)
    url = serializers.HyperlinkedIdentityField(
        view_name= 'product-detail',
        lookup_field = 'pk'
    )

    name = serializers.CharField(validators = [validators.validate_name,
                                               validators.unique_product_title,
                                               validators.validate_name_no_hello])
    class Meta:
        model = Product_model
        fields = [
            'owner',
            'pk',
            'url',
            'edit_url',
            'name',
            'content',
            'price',
            'sale_price',
        ]

    def get_my_user_data(self,obj):
        return {
            "username": obj.user.username
        }
    
    def validate_name(self, value):
        request= self.context.get('request')
        user = request.user
        qs = Product_model.objects.filter(user=user,name__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value

    def get_edit_url(self,obj):
        request= self.context.get('request')
        if request is None:
            return None
        return reverse("edit_url", kwargs={"pk":obj.pk}, request=request)
