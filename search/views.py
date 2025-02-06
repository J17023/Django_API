from rest_framework import generics
from products.models import Product_model
from products.serializers import Product_serializer

# Create your views here.

class SearchListView(generics.ListAPIView):
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
