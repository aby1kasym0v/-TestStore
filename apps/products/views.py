from django.shortcuts import render
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .filters import ProductFilter

# Create your views here.

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'



class ProductPaginations(PageNumberPagination):
    page_size = 2
    page_size_query_param = page_size
    max_page_size = 20


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    filterset_fields = ['category']  
    search_fields = ['name']  
    ordering_fields = ['price', 'popularity']  
    pagination_class = ProductPaginations





