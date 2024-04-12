from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('register/',views.registerpage, name = 'registerpage'),
    path('login/',views.loginpage, name = 'loginpage'),
    path('logout/',views.logoutuser, name = 'logout'),
    
    path('user/',views.userpage, name = 'userpage'),
    path('account_settings/',views.account_settings , name = 'account_settings'),
    
    path('home/',views.home, name = 'home'),    
    path('products/',views.products, name = 'products'),
    path('customer/<str:pk>',views.customer, name = 'customer'),
    
    path('create_order/<str:pk>',views.create_order, name = 'create_order'),
    path('update_order/<str:pk>',views.update_order, name = 'update_order'),
    path('delete_order/<str:pk>',views.delete_order, name = 'delete_order'),
    
    path('reset_password/',auth_view.PasswordResetView.as_view(), name= 'reset_password'),
    path('reset_password_sent/',auth_view.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(),name ='password_reset_confirm'),
    path('reset_password_complete/',auth_view.PasswordResetCompleteView.as_view(),name = 'password_reset_complete'),
    
    
]
