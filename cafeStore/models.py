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


