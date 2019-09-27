from django.shortcuts import render, redirect


def home(request):
    return redirect('dashboard')


def login(request):
    return render(request, "html/login.html", {})


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "html/dashboard.html", {})
    return redirect('login')