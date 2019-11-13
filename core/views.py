from django.shortcuts import render
from django.views import View
from product.models import Product
# Create your views here.

# class HomeView(View):
#     def get(self, request):
#         Products = {'Products': Product.objects.all()}
#         return render(request, 'homepage/index.html', Products)

def Home(request):
    Products = {'Products': Product.objects.all()}
    return render(request, 'homepage/index.html', Products) 
   