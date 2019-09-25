from django.shortcuts import render, redirect
from product.forms import *

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
