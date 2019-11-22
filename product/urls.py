from django.urls import path
from .views import ProductDetailView, CategoryView

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', ProductDetailView, name='product-detail'),
    path('category/', CategoryView.as_view(), name='category'),
]
