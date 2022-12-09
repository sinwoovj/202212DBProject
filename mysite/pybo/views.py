from django.shortcuts import render

# Create your views here.
from . import models
# from django.http import HttpResponse

def home(request):
    designer = models.Designer.objects.filter(name__contains='홍')
    print(designer)
    return render(request, 'html/home.html', {'designer' : designer})

def index(request):
    return render(request, 'html/index.html')

def highlight(request):
    return render(request, 'html/highlight.html')

def record(request):
    return render(request, 'html/record.html')

def rank(request):
    return render(request, 'html/rank.html')

