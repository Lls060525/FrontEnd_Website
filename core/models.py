from django.db import models

# Create your models here.
from django.db import models

class HeroProduct(models.Model):
    name = models.CharField(max_length=100, default="FH-ELITE")
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CategoryCard(models.Model):
    title = models.CharField(max_length=50) # e.g., "COLLECTION"
    subtitle = models.CharField(max_length=50) # e.g., "01 / ARCHIVES"
    image = models.ImageField(upload_to='categories/')
    order = models.IntegerField(default=0) # To keep them in 1, 2, 3 order

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class CatalogSection(models.Model):
    title = models.CharField(max_length=100) # e.g., "Collections", "Innovation"
    subtitle = models.CharField(max_length=200, blank=True)
    background_image = models.ImageField(upload_to='sections/')

    def __str__(self):
        return self.title

class Product(models.Model):
    section = models.ForeignKey(CatalogSection, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name