from django.contrib import admin
from .models import Product, Transaction

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'thumbnail','price', 'flash_deal', 'user_id', 'description']
    search_fields = ['product']
    list_filter = ['price']
    list_per_page = 10

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'user_id']
    search_fields = ['id', 'product_id', 'user_id']
    list_filter = ['id', 'product_id', 'user_id']
    list_per_page = 10

admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)