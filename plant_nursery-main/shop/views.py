from django.shortcuts import render, get_object_or_404
from .models import Category, Plant

def home(request):
    categories = Category.objects.all()
    plants = Plant.objects.all()
    return render(request, 'shop/home.html', {'categories': categories, 'plants': plants})



def category_plants(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    plants = Plant.objects.filter(category=category)
    return render(request, 'shop/category_plants.html', {
        'category': category,
        'plants': plants
        
    })


def plant_detail(request, slug):
    plant = get_object_or_404(Plant, slug=slug)
    return render(request, 'shop/plant_detail.html', {'plant': plant})
