from django.shortcuts import render
from django.views import View
from product.models import Product
# Create your views here.

# class HomeView(View):
#     def get(self, request):
#         Products = {'Products': Product.objects.all()}
#         return render(request, 'homepage/index.html', Products)

def Home(request):
    Active_Products = filter(lambda product: product.active, Product.objects.all())
    Products = {'Products': Active_Products}
    return render(request, 'homepage/home.html', Products) 
   