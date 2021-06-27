import json
from math import ceil

from .models import *

def cookiesCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total': 0,'get_original_cart_total':0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_total']

    for i in cart:
        cartItems += cart[i]['quantity']
        product = CafeProducts.objects.get(id=i)
        total = (product.discountPrice * cart[i]['quantity'])
        print(total)
        originalTotal = (product.price * cart[i]['quantity'])
        order['get_cart_total'] += total
        order['get_original_cart_total'] += originalTotal
        order['get_cart_items'] += cart[i]['quantity']
        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'discription': product.description,
                'category': product.category,
                'rate': product.rate,
                'savePrice': product.savePrice,
                'price': product.price,
                'tags': product.tags,
                'discountPrice': product.discountPrice,
                'image': product.image.url,
                'in_stock': product.in_stock,

            },
            'quantity': cart[i]['quantity'],
            'get_total': total,
            'get_original_total': originalTotal,
        }
        items.append(item)

    return {'cartItems':cartItems, 'order':order, 'items':items, 'save': order['get_original_cart_total'] - order['get_cart_total']}


def cartData(request):
    if request.user.is_authenticated:
        customer = User.objects.get(id=request.user.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        save = order.get_original_cart_total - order.get_cart_total
    # print('created order', created)
    else:
        cookiesData = cookiesCart(request)
        items = cookiesData['items']
        order = cookiesData['order']
        cartItems = cookiesData['cartItems']
        save = cookiesData['save']


    return {'cartItems':cartItems, 'order':order, 'items':items, 'save': save}



