from django.shortcuts import render, redirect
from .forms import *
from accounts.models import User
from .models import Staff

# Create your views here.


def create_new(request):
    if request.method == 'POST':
        add_staff_form = AddStaffForm(request.POST)
        if add_staff_form.is_valid():
            email = add_staff_form.cleaned_data.get('email')
            full_name = add_staff_form.cleaned_data.get('full_name')

            is_ProcueStaff = add_staff_form.cleaned_data.get('is_ProcueStaff')
            is_HRStaff = add_staff_form.cleaned_data.get('is_HRStaff')
            is_DeliveryStaff = add_staff_form.cleaned_data.get('is_DeliveryStaff')
            is_Accountant = add_staff_form.cleaned_data.get('is_Accountant')
            is_SiteManager = add_staff_form.cleaned_data.get('is_SiteManager')
            is_Inspector = add_staff_form.cleaned_data.get('is_Inspector')

            print(email)

            user_obj = User.objects.create_staffuser(email,'1234')
            Staff.objects.create(user=user_obj,
                                 name=full_name,
                                 is_ProcueStaff=is_ProcueStaff,
                                 is_HRStaff=is_HRStaff,
                                 is_DeliveryStaff=is_DeliveryStaff,
                                 is_Accountant=is_Accountant,
                                 is_SiteManager=is_SiteManager,
                                 is_Inspector=is_Inspector)
            return redirect('dashboard')
    else:
        add_staff_form = AddStaffForm()
    context = {
        'form': add_staff_form,
    }
    return render(request, "staff/add_staff_member.html", context)
