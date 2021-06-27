from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal

# Create your models here.
class CafeProducts(models.Model):
    category_choice = [
        ('coffee_and_tea', 'COFFEE AND TEA'),
        ('beverages', 'BEVERAGES'),
        ('munchies', 'MUNCHIES'),
        ('desert', 'DESERT'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=100, choices=category_choice)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=16, decimal_places=2)
    savePrice = models.DecimalField(max_digits=16, decimal_places=2)
    rate = models.PositiveIntegerField()
    discountPrice = models.DecimalField(max_digits=16, decimal_places=2)
    in_stock = models.BooleanField()
    tags = models.TextField(max_length=500, null=True, blank=True, default="")
    weight = models.IntegerField()
    pack = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return  str(self.id)

    @property
    def shipping(self):
        shipping = False
        order_items = self.orderitem_set.all()
        for i in order_items:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_original_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_original_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total


class OrderItem(models.Model):
    status_category = (
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Shipping", "Shipping"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered")
    )
    product = models.ForeignKey(CafeProducts, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, choices=status_category, default="Pending")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product.discountPrice * self.quantity
        return total

    @property
    def get_original_total(self):
        total = self.product.price * self.quantity
        return total