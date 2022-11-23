from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class ShopItem(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name