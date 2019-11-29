from django.shortcuts import render, get_object_or_404, HttpResponse, get_list_or_404
from django.views import View
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class ProductDetailView(View):
    def get(self, request, pk):
        single_product = {"Product": get_object_or_404(Product, pk=pk)} 
        return render(request, 'product/product-details.html', single_product)

def CategoryView(request, slug):
    categories_parents = Category.objects.all().filter(parent_Id__isnull=True)
    category = Category.objects.get(slug=slug) 
    products = Product.objects.all().filter(category=category)
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        list_products = paginator.page(page)
    except PageNotAnInteger:
        list_products = paginator.page(1)
    except EmptyPage:
        list_products = paginator.page(paginator.num_pages)
    Data = {"Categories_parents": categories_parents, "Products": list_products}
    return render(request, 'product/category.html', Data)

    # def post(self, request):
    #     products_category = get_list_or_404(Product, category=pk)