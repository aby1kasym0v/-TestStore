from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')                                  # Имя продукта
    total_price = serializers.ReadOnlyField()                                                  # Цена за все единицы продукта

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'product_name', 'quantity', 'total_price', 'slug', 'created_at', 'updated_at']
