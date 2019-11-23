from django.shortcuts import render, get_object_or_404, HttpResponse, get_list_or_404
from django.views import View
from .models import Product, Category
# Create your views here.

class ProductDetailView(View):
    def get(self, request, pk):
        single_product = {"Product": get_object_or_404(Product, pk=pk)}
        return render(request, 'product/product-details.html', single_product)

class CategoryView(View):
    def get(self, request, ):
        categories = {"Categories": Category.objects.all()}
        return render(request, 'product/category.html', categories)

    def post(self, request):
        products_category = get_list_or_404(Product, category=pk)