from django.urls import path, include
from .views import ProductAPIView, CategoryDetailView
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),  
    path('products/', ProductAPIView.as_view(), name='product-list'),                 
]
