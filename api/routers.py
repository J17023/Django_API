from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductGenericViewSet
from django.urls import path, include

router = DefaultRouter()

router.register('products-abc', ProductGenericViewSet, basename="products")

urlpatterns = router.urls
