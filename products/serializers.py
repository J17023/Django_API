from rest_framework import serializers
from .models import Product_model
from rest_framework.reverse import reverse
from . import validators

class Product_serializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only =  True)
    edit_url = serializers.SerializerMethodField(read_only= True)
    url = serializers.HyperlinkedIdentityField(
        view_name= 'product-detail',
        lookup_field = 'pk'
    )

    name = serializers.CharField(validators = [validators.validate_name,
                                               validators.unique_product_title,
                                               validators.validate_name_no_hello])
    title = serializers.CharField(source = 'name', read_only = True)
    class Meta:
        model = Product_model
        fields = [
            #'user',
            'pk',
            'url',
            'edit_url',
            'name',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def validate_name(self, value):
        request= self.context.get('request')
        user = request.user
        qs = Product_model.objects.filter(user=user,name__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value

#     def create(self, validated_data):
#          email = validated_data.pop('email')
#         obj= super().create(validated_data)
#         print(email,obj)
#         return obj

#     def update(self,instance, validated_data):
#         instance.title = validated_data.get('title')
#         return instance


    def get_edit_url(self,obj):
        request= self.context.get('request')
        if request is None:
            return None
        return reverse("edit_url", kwargs={"pk":obj.pk}, request=request)
    
    def get_my_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None