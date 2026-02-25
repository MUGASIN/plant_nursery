from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.category_plants, name='category_plants'),
    path('plant/<slug:slug>/', views.plant_detail, name='plant_detail'),
]
