from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Plant
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def cart_add(request, plant_id):
    cart = Cart(request)
    plant = get_object_or_404(Plant, id=plant_id)
    cart.add(plant=plant, quantity=1)
    return redirect('cart:cart_detail')

def cart_remove(request, plant_id):
    cart = Cart(request)
    plant = get_object_or_404(Plant, id=plant_id)
    cart.remove(plant)
    return redirect('cart:cart_detail')
