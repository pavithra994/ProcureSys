from django.shortcuts import render, redirect
from order.models import Order


def home(request):
    return redirect('dashboard')


def login(request):
    return render(request, "html/login.html", {})


def dashboard(request):

    if request.user.is_authenticated:
        order_qs = None
        if request.user.is_supplier:
            order_qs = None
        elif request.user.is_staff and not request.user.is_admin:
            if request.user.staff.is_SiteManager:
                order_qs = Order.objects.filter(Status="Pending")
        else:
            try:
                order_qs = request.user.staff.order_set.all()
            except Exception as e:
                pass

        context = {
            "order_qs":order_qs,
        }
        return render(request, "html/dashboard_updated.html", context)
    return redirect('login')