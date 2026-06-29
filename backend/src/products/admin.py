from django.contrib import admin

from products.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'id']
    search_fields = ['name']
    readonly_fields = ['slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'price', 'slug', 'id']
    search_fields = ['name']
    readonly_fields = ['id', 'slug']