# core views.py
from django.shortcuts import render

from django.shortcuts import render
from .models import HeroProduct, CategoryCard, CatalogSection


def home(request):
    product = HeroProduct.objects.filter(is_active=True).last()
    # Fetch all category cards sorted by order
    categories = CategoryCard.objects.all()
    return render(request, 'core/index.html', {
        'product': product,
        'categories': categories
    })

def learn_more(request):
    return render(request, 'core/learn_more.html')


def collections_view(request):
    # Fetch categories for the top slider (as seen in image_1d3a20.png)
    categories = CategoryCard.objects.all()
    # Fetch all catalog sections and their related products
    catalog_sections = CatalogSection.objects.prefetch_related('products').all()

    return render(request, 'core/collections.html', {
        'categories': categories,
        'catalog_sections': catalog_sections
    })
