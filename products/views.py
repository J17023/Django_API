from rest_framework import generics, permissions,authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product_model
from .serializers import Product_serializer
from .permissions import IsStaffEditorPermisison

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product_model.objects.all()
    serializer_class = Product_serializer
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermisison]

    def perform_create(self,serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = name 
            
        serializer.save(content = content)

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product_model.objects.all()
    serializer_class = Product_serializer()

    def perform_create(self,serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = name 
            
        serializer.save(content = content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product_model.objects.all()
    serializer_class = Product_serializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product_model.objects.all()
    serializer_class = Product_serializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.name 

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product_model.objects.all()
    serializer_class = Product_serializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

        

@api_view(['GET','POST'])
def product_alt_view(request,pk = None, *args,**kwargs):

    method = request.method

    if method == 'GET': 
        if  pk == None:
            qs = Product_model.objects.all()
            data = Product_serializer(qs,many = True).data
            return Response(data)

        obj = get_object_or_404(Product_model, pk=pk)
        return Response(data)

    if method == 'POST':
        serializer = Product_serializer(data=request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content = name 
            
            serializer.save(content = content)
            return Response(serializer.validated_data)
        
        return Response({"error": "el usuario no se puede agregar"},status=400)