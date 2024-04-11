from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerpage, name = 'registerpage'),
    path('login/',views.loginpage, name = 'loginpage'),
    path('logout/',views.logoutuser, name = 'logout'),
    
    path('user/',views.userpage, name = 'userpage'),
    
    path('home/',views.home, name = 'home'),    
    path('products/',views.products, name = 'products'),
    path('customer/<str:pk>',views.customer, name = 'customer'),
    
    path('create_order/<str:pk>',views.create_order, name = 'create_order'),
    path('update_order/<str:pk>',views.update_order, name = 'update_order'),
    path('delete_order/<str:pk>',views.delete_order, name = 'delete_order'),
]
