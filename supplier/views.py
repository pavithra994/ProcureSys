from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.

def supplierhome(request):
    supplier_qs = Supplier.objects.all()
    context = {
        "supplier_qs":supplier_qs,
    }
    return render(request, 'supplier/supplier_homepage.html', context)

def displaySupplierProducts(request):
    info = SupplierProductInfo.objects.all()
    for i in info:
        if i.Qty == 0:
            i.Status = "Out of Stock"
            i.save()
        else:
            i.Status = "Available"
            i.save()
    queryset = SupplierProductInfo.objects.all()
    total = 0
    for instance in queryset:
        total += instance.net_price_item
    context = {'info': info,
               'total': total,
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

def add_new_supplier(request):
    if request.method == 'POST':
        add_supplier_form = AddSupplierForm(request.POST)
        if add_supplier_form.is_valid():
            email = add_supplier_form.cleaned_data.get('email')
            full_name = add_supplier_form.cleaned_data.get('full_name')

            user_obj = User.objects.create_supplieruser(email,'1234')
            Supplier.objects.create(user=user_obj,name=full_name)
            return redirect('dashboard')
    else:
        add_supplier_form = AddSupplierForm()
    context = {
        'form': add_supplier_form,
    }
    return render(request, "supplier/add_new_supplier.html", context)

def supplieritemalysis(request):
    qs1 = SupplierProductInfo.objects.all()
    qs2 = SupplierProductInfo.objects.all().filter(Status='Available')
    qs3 = SupplierProductInfo.objects.all().filter(Status='Reserved')
    qs4 = SupplierProductInfo.objects.all().filter(Status='Out_Of_Stock')

    numberOfItems = qs1.count()
    numberOfAvaliable = qs2.count()
    numberOfReserved= qs3.count()
    numberOfOutofstock = qs4.count()

    net_price_item = 0
    for i in qs1:
        net_price_item += i.net_price_item

    net_price_available_item = 0
    for i in qs2:
        net_price_available_item += i.net_price_item

    net_price_Reserved_item = 0
    for i in qs3:
        net_price_Reserved_item += i.net_price_item

    net_price_outofstock_item = 0
    for i in qs4:
        net_price_outofstock_item += i.net_price_item

    context ={
        'numberOfItems' : numberOfItems,
        'numberOfAvaliable' : numberOfAvaliable,
        'numberOfReserved' : numberOfReserved,
        'numberOfOutofstock': numberOfOutofstock,
        'net_price_item' : net_price_item,
        'net_price_available_item': net_price_available_item,
        'net_price_Reserved_item': net_price_Reserved_item,
        'net_price_outofstock_item': net_price_outofstock_item,
    }

    return render(request, 'supplier/analysis.html', context)

def get_queryset(Status, Qty):
   if Qty == 0:
    return Status == 'Out_Of_Stock'