from django.shortcuts import render, redirect, get_object_or_404
from order.forms import *
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
    invoice = Invoice()
    for item in info:
        if item.amount > 100000:
            item.Status = "Pending"
        elif item.Status == "Pending":
            item.approval = "Pending"
            item.save()
        else:
            item.Status = "Approved"
            item.approval = "Pending"
            item.save()
    invoice.order_id = infor.slug
    invoice.date = infor.date
    invoice.amount_due = infor.amount
    invoice.save()
    context = {'info': info}
    print(infor)
    return render(request, 'order/order_details.html', context)

def editOrder(request, pk):
    item = get_object_or_404(Order, pk = pk)

    if request.method =="POST":
        form = OrderPlacementForm(request.POST,instance=item)

        if form.is_valid():
            form.save()
            return redirect('viewPurchase')

    else:
        form = OrderPlacementForm(instance=item)
        return render(request, "order/editOrder.html", {'form': form})
def deleteOrder(request, pk):
    Order.objects.filter(pk=pk).delete()
    info = Order.objects.all()
    context = {'info': info}
    return render(request, 'order/viewPurchaseOrder.html', context)

def addTender(request):
    if request.method == 'POST':
        form = AddTender(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewPurchase')
    else:
        form = AddTender()
    return render(request,'order/addTender.html',{'form':form})



