from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from products.models import Category, Product
from products.serializers import (
    CategorySerializer,
    ProductSerializer
)

class CategoriesView(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class ProductsViewset(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'slug'