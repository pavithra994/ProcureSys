
from django.contrib import admin
from django.urls import path
from . import views
from accounts.views import login_page
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.home,name='home'),
    path('login/',login_page,name='login'),
    path('dashbotharukaard/',views.dashboard, name='dashboard'),
    path('supplier/',include('supplier.urls')),
    path('product/', include('product.urls')),
]
