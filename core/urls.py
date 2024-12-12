from rest_framework.routers import DefaultRouter
from apps.users.views import RegisterApiView
from apps.products.views import ProductAPIView
from apps.cart.views import CartAPIViewSet
from django.contrib import admin
from django.urls import path, include


router = DefaultRouter()


router.register(r'users/', RegisterApiView)
router.register(r'products/', ProductAPIView)
router.register(r'cart/', CartAPIViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')), 
    path('api/', include('apps.products.urls')), 
    path('api/', include('apps.cart.urls'))
]