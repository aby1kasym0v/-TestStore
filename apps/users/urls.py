from django.urls import path
from .views import RegisterApiView, LoginView

urlpatterns = [
    path('auth/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
