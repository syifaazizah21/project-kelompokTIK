from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product = models.CharField(max_length=200)
    price = models.IntegerField()
    thumbnail = models.ImageField(null=True, blank=True, upload_to='thumbnail/')
    description = models.TextField()
    flash_deal = models.BooleanField(null=True, blank=True)
    user_id = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.product

class Transaction(models.Model):
    product_id = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __int__(self):
        return self.id