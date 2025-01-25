from django.db import models

# Create your models here.

class Product_model_version_one(models.Model):
    name = models.CharField( max_length=50)
    content = models.TextField(blank= True, null= True)
    price = models.DecimalField( max_digits=5,decimal_places=2, default=99.9)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return 122
