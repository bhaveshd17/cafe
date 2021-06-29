
from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('updateItem/', views.updateItem, name='updateItem'),
    path('userInfo/<int:pk>/', views.userInfo, name='userInfo'),

    path('login/', views.handleLogin, name='login'),
    path('signin/', views.handleSignIp, name='signin'),
]
