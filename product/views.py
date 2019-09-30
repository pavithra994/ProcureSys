from django.shortcuts import render, redirect
from product.forms import *
from supplier.models import SupplierProductInfo

def add_product_types(request):
    if request.method == 'POST':
        form = AddProductTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddProductTypeForm()
    return render(request, 'product/add_product_type.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddProductForm()
    return  render(request, 'product/add_product.html', {'form': form})


def product_details(request):
    qs = ''
    if request.user.is_supplier:
        supplier_user = request.user.supplier
        # for sup_product in supplier_user.supplierproductinfo_set:
        #     sup_product.
        qs = supplier_user.supplierproductinfo_set.all()

    product_supplier_qs = SupplierProductInfo.objects.all()
    product_type_qs = Product.objects.all()
    context = {
        'product_qs': qs,
        'product_supplier_qs':product_supplier_qs,
        'product_type_qs':product_type_qs,
    }

    return render(request,'product/product_info.html',context)