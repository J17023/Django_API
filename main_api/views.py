from django.shortcuts import render
from .models import Product_model_version_one
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Product_serializer

# Create your views here.

@api_view(['POST'])
def api_home(request):
    serialized_data = Product_serializer(data = request.data)

    if  serialized_data.is_valid():
        #instance= serialized_data.save()
        print(serialized_data.data)
        return Response(serialized_data.data)

    