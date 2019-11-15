from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product
# Create your views here.

def ProductDetailView(request, pk):
    single_product = {"Product": get_object_or_404(Product, pk=pk)}
    return render(request, 'product/product-details.html', single_product)