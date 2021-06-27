from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import *
from .utils import cartData
import json

def home(request):
    data = cartData(request)
    product_obj = CafeProducts.objects.all()
    cartItems = data['cartItems']
    content = {'product_obj':product_obj,
               'cartItems':cartItems}
    return render(request, 'store/home.html', content)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.id
    product = CafeProducts.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item added', safe=False)

def cart(request):
    data = cartData(request)
    items = data['items']
    cartItems = data['cartItems']
    order = data['order']
    content = {'items':items, 'cartItems':cartItems, 'order':order, 'save':data['save']}
    return render(request, 'store/cart.html', content)


