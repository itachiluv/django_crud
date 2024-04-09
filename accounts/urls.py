from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name = 'home'),    
    path('products/',views.products, name = 'products'),
    path('customer/',views.customer, name = 'customer'),
]
