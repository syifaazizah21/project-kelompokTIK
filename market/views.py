from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
    flashDeal = Product.objects.all()
    newProducts = Product.objects.all()[:5]
    
    context = {
        'flash': flashDeal,
        'newProduct': newProducts
    }
    
    
    return render(request, 'index.html', context)

def marketPlace(request):
    product= Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'market-place.html', context)

def transaction(request):
    return render(request, 'transaction.html')

def addProduct(request):
    return render(request, 'add-product.html')

def addProductRecord(request):
    product = request.POST['product']
    price = request.POST['price']
    thumbnail = request.FILES['thumbnail']
    desc = request.POST['description']
    flash = request.POST.get('flash', False)
    
    # Process request from client
    newProduct = Product(product=product, price=price, description=desc, thumbnail=thumbnail, flash_deal=flash)
    newProduct.save()
    return redirect('/market-place/')

def updateProduct(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'update-product.html', context)

def updateProductRecord(request, id):
    productName = request.POST['product']
    price = request.POST['price']
    desc = request.POST['description']
    
    products = Product.objects.get(id=id)
    products.product = productName
    products.price = price
    products.desc = desc
    products.save()
    
    return redirect('/market-place/')

def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/market-place/')