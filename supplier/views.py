from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def supplierhome(request):
    return render(request, 'supplier/supplier_homepage.html')

def displaySupplierProducts(request):
    info = SupplierProductInfo.objects.all()
    context = {'info': info,
               'dashboard_dir': 'SupplierProductInfo'}
    return render(request, 'supplier/supplier_productpage.html',context)