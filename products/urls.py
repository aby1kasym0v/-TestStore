from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CartAPIView, CartItemDeleteAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('cart/', CartAPIView.as_view(), name='cart'),
    path('cart/<int:product_id>/', CartItemDeleteAPIView.as_view(), name='cart-delete'),
]
