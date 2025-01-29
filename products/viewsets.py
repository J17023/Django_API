from rest_framework import viewsets, mixins

from .models import  Product_model
from .serializers import Product_serializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product_model.objects.all()
    serializer_class = Product_serializer

class ProductGenericViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    queryset= Product_model.objects.all()
    serializer_class = Product_serializer    
