from django.urls import path
from.import views
from django.conf.urls import url

urlpatterns =[
path('',views.supplierhome, name='supplierhomepage'),
path('display/',views.displaySupplierProducts, name='displaySupplierProducts'),
path('addsupplierinfo/', views.supplierinfoform, name='addsupplierinfo'),

url(r'^edit_supplieritem/(?P<pk>\d+)' , views.edit_supplieritem, name='edit_supplieritem'),
]