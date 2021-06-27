
from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('updateItem/', views.updateItem, name='updateItem'),

]
