from django.shortcuts import render, HttpResponse
from .models import *

def home(request):
    product_obj = CafeProducts.objects.all()
    content = {'product_obj':product_obj}
    return render(request, 'store/home.html', content)
