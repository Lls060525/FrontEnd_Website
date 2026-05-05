from django.contrib import admin

# Register your models here.
from .models import HeroProduct, CategoryCard, CatalogSection, Product

admin.site.register(HeroProduct)

admin.site.register(CategoryCard)

@admin.register(CatalogSection)
class CatalogSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'price')
    list_filter = ('section',)