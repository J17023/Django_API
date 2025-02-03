from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL
class Product_model(models.Model):
    user = models.ForeignKey(User,null= True, default=1, on_delete=models.SET_NULL)
    name = models.CharField( max_length=50)
    content = models.TextField(blank= True, null= True)
    price = models.DecimalField( max_digits=5,decimal_places=2, default=99.9)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return 122
