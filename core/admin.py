from django.contrib import admin

# Register your models here.
from .models import HeroProduct, CategoryCard

admin.site.register(HeroProduct)

admin.site.register(CategoryCard)