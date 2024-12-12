from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    slug = models.SlugField(max_length=155 , unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    popularity = models.IntegerField(default=0)
    slug = models.SlugField(max_length=155, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
