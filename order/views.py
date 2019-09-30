from django.shortcuts import render, redirect, get_object_or_404
from order.forms import OrderPlacementForm
from order.models import *

def order_placement(request):
    if request.method == 'POST':
        form = OrderPlacementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = OrderPlacementForm()
    return render(request, 'order/order_placement.html', {'form': form})

def display_order_request(request):
    info = Order.objects.all()
    for item in info:
        if item.amount > 100000:
            item.Status = "Pending"
            item.save()
        else:
            item.Status = "Order Placed"
            item.save()
    context = {'info': info}
    return render(request, 'order/order_details.html', context)

def approval_request(request, pk):
    infor = get_object_or_404(Order, pk=pk)
    info = Order.objects.all()
    for item in info:
        if item.amount > 100000:
            item.Status = "Pending"
            item.save()
        else:
            item.Status = "Order Placed"
            item.save()
    context = {'info': info}
    print(infor)
    return render(request, 'order/order_details.html', context)
