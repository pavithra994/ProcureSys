from django.shortcuts import render, redirect, get_object_or_404
from order.forms import *
from order.models import *
import logging

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
            tender = form.save()
            logging.info(type(tender))
            tender.site = request.user.staff
            tender.save()

            return redirect('addTender')
    else:
        form = AddTender()
    return render(request,'order/addTender.html',{'form':form})


def request_order(request):
    total = 0
    if request.user.is_staff and not request.user.is_admin:
        tender_qs = request.user.staff.tender_set.filter(proceed=False)
        if request.method == 'POST':
            form = AddTender(request.POST)
            if form.is_valid():
                tender = form.save()
                logging.info(type(tender))
                tender.site = request.user.staff
                tender.save()

                return redirect('addTender')
        else:
            form = AddTender()
            for tender in tender_qs:
                total += tender.get_amount()

        context = {
            'tender_qs' : tender_qs,
            'form':form,
            'total':total
        }
        return render(request,'order/request.html',context)
    else:
        return render(request,"html/404.html",{'error':"Sign in as a supplier"})


def proceed_order(request):
    total = 0
    tender_qs = request.user.staff.tender_set.filter(proceed=False)
    tender_list = []
    for tender in tender_qs:
        total += tender.get_amount()

    if request.method == 'POST':
        form = OrderPlacementForm(request.POST)
        if form.is_valid():
            order = form.save()
            for tender in list(tender_qs):
                tender.proceed = True
                tender.save()
                tender_list.append(tender)
            order.product_and_quantity.add(*tender_list)
            order.amount = total
            order.site = request.user.staff
            # if total < 100000.0:
            #     order.Status = "Approved"
            # else:
            #     order.Status = "Pending"
            order.set_status()
            order.save()
            return redirect('dashboard')
    else:
        form = OrderPlacementForm()
    context = {
        'form': form,
        'tender_qs': tender_qs
    }
    return render(request,'order/order_placement.html',context)






