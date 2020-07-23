from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return  render(request, 'myapp/index.html')

def home(request, name):
    return  render(request, 'myapp/Home.html', {'name':name})

def facto(request, num):
    res = 1
    for i in range(1, int(num)+1):
        res *= i

    return HttpResponse(f"<h1>The factorial number is:{res}</h1>")
