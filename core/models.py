from django.db import models

# Create your models here.
from django.db import models

class HeroProduct(models.Model):
    name = models.CharField(max_length=100, default="FH-ELITE")
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name