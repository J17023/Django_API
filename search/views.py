from rest_framework import generics
from products.models import Product_model
from products.serializers import Product_serializer
from rest_framework.response import Response
from . import client
# Create your views here.

class SearchListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        tag = request.GET.get('tag')
        if not query:
            return Response('', status=400)
        results = client.perform_search(query, tags = tag)
        return Response(results)

class SearchListOldView(generics.ListAPIView):
    queryset = Product_model.objects.all()
    serializer_class = Product_serializer

    def get_queryset(self,*args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        results = qs.search(q, user = user)
        return results
