from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product_model

@register(Product_model)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields=[
        'name',
        'content',
        'price',
        'public',
    ]
    
    tags = 'get_tags_list'
