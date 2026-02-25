from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('payment_success/<int:order_id>/', views.payment_success, name='payment_success'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('', views.order_list, name='order_list'),  # ✅ ADD THIS
]
