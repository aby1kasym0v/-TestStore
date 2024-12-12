from django.urls import path, include
from .views import CartAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cart', CartAPIViewSet, basename='cart')

urlpatterns = [
    path('cart/<slug:slug>', include(router.urls)),
]