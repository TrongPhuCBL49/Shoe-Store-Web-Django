from django.contrib import admin
from .models import Category, Product, Variation
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'active']
    list_filter = ['active']
    search_fields = ['title']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'active']
    list_filter = ['category', 'active']
    search_fields = ['title']
admin.site.register(Product, ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'title', 'price', 'sale_price', 'inventory', 'active']
    list_filter = ['product']
    search_fields = ['title']
admin.site.register(Variation, VariationAdmin)
