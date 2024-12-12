from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from rest_framework.decorators import action
# Create your views here.
class CartAPIViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)# Показывать только корзину текущего пользователя

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # Указать текущего пользователя при добавлении в корзину

    @action(detail=False, methods=['get'], url_path='summary')
    def cart_summary(self, request):
        # Обзор корзины с общей суммой
        cart_items = self.get_queryset()
        total = sum(item.total_price for item in cart_items)
        return Response({'cart_items': CartSerializer(cart_items, many=True).data, 'total_price': total})
