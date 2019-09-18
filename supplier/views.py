from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def supplierhome(request):
    return render(request, 'supplier/supplier_homepage.html')