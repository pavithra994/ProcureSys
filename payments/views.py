from django.shortcuts import render
from .models import Payments

# Create your views here.
def payment_page(request):
    payment_qs = Payments.objects.filter(done=False)
    payment_done_qs =  Payments.objects.filter(done=True)

    context = {
        'payment_qs':payment_qs,
        'payment_done_qs':payment_done_qs
    }

    return render(request,"payments/payment_page.html",context)
