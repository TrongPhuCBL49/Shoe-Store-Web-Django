from django.urls import path
from .views import ProductDetailView

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', ProductDetailView, name='product-detail'),
]
