from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import LoginForm
from .models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = LoginForm(request.POST or None)
    error = ' '
    print(request.user.is_authenticated)

    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        print('email - {} password - {}'.format(email,password))
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print("login success")
            return redirect('dashboard')
        else:
            error = 'error'
            print('Error')

    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'html/login.html', context)