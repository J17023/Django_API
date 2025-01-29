from rest_framework import serializers
from .models import Product_model
from rest_framework.reverse import reverse

class Product_serializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only =  True)
    edit_url = serializers.SerializerMethodField(read_only= True)
    url = serializers.HyperlinkedIdentityField(
        view_name= 'product-detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Product_model
        fields = [
            'pk',
            'url',
            'edit_url',
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

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