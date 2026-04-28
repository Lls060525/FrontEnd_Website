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