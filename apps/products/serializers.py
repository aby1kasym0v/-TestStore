from apps.products.models import Product, Category
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True, read_only = True)
    class Meta:
        model = Category
        fields = '__all__'