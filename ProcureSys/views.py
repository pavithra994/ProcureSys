from django.shortcuts import render


def home(request):
    return render(request, "html/index.html", {})


def login(request):
    return render(request, "html/login.html", {})


def dashboard(request):
    return render(request, "html/dashboard.html", {})