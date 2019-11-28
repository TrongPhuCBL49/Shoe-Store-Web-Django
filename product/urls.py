from django.urls import path
from .views import ProductDetailView, CategoryView

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('category/<slug:slug>/', CategoryView, name='category'),
]
