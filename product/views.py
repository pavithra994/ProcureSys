from django.shortcuts import render, redirect
from product.forms import *

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
