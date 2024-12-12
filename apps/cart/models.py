from django.db import models
from apps.users.models import User
from apps.products.models import Product
from django.utils.text import slugify

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    slug = models.SlugField(max_length=155, unique=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)           # Количество товаров
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.quantity}'
    
    @property
    def total_price(self):
        return self.quantity * self.product.price