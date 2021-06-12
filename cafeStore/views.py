from django.shortcuts import render, HttpResponse

def home(request):
    content = {}
    return render(request, 'store/home.html', content)
