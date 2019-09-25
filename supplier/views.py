from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.

def supplierhome(request):
    return render(request, 'supplier/supplier_homepage.html')

def displaySupplierProducts(request):
    info = SupplierProductInfo.objects.all()
    context = {'info': info,
               'dashboard_dir': 'SupplierProductInfo'}
    return render(request, 'supplier/supplier_productpage.html',context)

def supplierinfoform(request):
    if request.method == "POST":
        form = SupplierProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('displaySupplierProducts')

    else:
        form = SupplierProductForm()
        return render(request, 'supplier/add_supplier.html',{'form':form})

def edit_supplieritem(request, pk):
    item = get_object_or_404(SupplierProductInfo, pk=pk)

    if request.method == "POST":
        form = SupplierProductForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('displaySupplierProducts')

    else:
        form = SupplierProductForm(instance=item)
        return render(request, 'supplier/edit_supplieritem.html', {'form': form})

def delete_supplieritem(request, pk):
    SupplierProductInfo.objects.filter(pk=pk).delete()
    info = SupplierProductInfo.objects.all()
    context = {'info': info}
    return render(request, 'supplier/supplier_productpage.html', context)