from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    context = {'products': products,}
    """"View function show all products including sorting queries."""
    return render(request, 'products/products.html',context)