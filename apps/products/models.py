from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    popularity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')