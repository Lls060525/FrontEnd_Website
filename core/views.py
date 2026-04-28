# core views.py
from django.shortcuts import render

from django.shortcuts import render
from .models import HeroProduct

def home(request):
    # Fetch the most recent active product
    product = HeroProduct.objects.filter(is_active=True).last()
    return render(request, 'core/index.html', {'product': product})


