# core views.py
from django.shortcuts import render

from django.shortcuts import render
from .models import HeroProduct, CategoryCard


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


