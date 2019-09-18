from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home1(request):
    return HttpResponse('<h1>Supplier Manegement Home Page</h1>')