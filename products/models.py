from django.db import models
from django.conf import settings
from django.db.models import Q


    
# Create your models here.
User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public = True)

    def search(self,query, user = None):
        lookup = Q(name__icontains = query) | Q(content__icontains = query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = qs.filter(user = user).filter(lookup)
            qs= (qs | qs2).distinct()
        return qs

class  ProductManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        return ProductQuerySet(self.model, using=self.db)
    
    def search(self,query, user= None):
        return self.get_queryset().search(query, user=user)
        
    
class Product_model(models.Model):
    user = models.ForeignKey(User,null= True, default=1, on_delete=models.SET_NULL, related_name= 'products')
    name = models.CharField( max_length=50)
    content = models.TextField(blank= True, null= True)
    price = models.DecimalField( max_digits=5,decimal_places=2, default=99.9)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return 122
