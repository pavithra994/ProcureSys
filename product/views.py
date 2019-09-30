from django.shortcuts import render, redirect, get_object_or_404
from product.forms import *
from supplier.models import SupplierProductInfo

def display_products(request):
    info = Product.objects.all()
    context ={ 'info': info }
    return render(request, 'product/product.html', context)

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


def edit_product(request, pk):
    item = get_object_or_404(Product, pk = pk)

    if request.method =="POST":
        form = AddProductForm(request.POST,instance=item)

        if form.is_valid():
            form.save()
            return redirect('display_products')

    else:
        form = AddProductForm(instance=item)
        return render(request, "product/manage_product.html", {'form': form})

def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    info = Product.objects.all()
    context = {'info': info}
    return render(request, 'product/product.html', context)
