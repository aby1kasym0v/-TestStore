from django.urls import path
from .views import ProductAPIView, CategoryDetailView

urlpatterns = [
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),  
    path('products/', ProductAPIView.as_view(), name='product-list'),                 
]
