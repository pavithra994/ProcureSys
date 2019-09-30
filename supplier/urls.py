from django.urls import path
from.import views
from django.conf.urls import url

urlpatterns =[
path('',views.supplierhome, name='supplierhomepage'),
path('add_product/',views.add_product,name="add_product"),
path('display/',views.displaySupplierProducts, name='displaySupplierProducts'),
path('display/addsupplierinfo/', views.supplierinfoform, name='addsupplierinfo'),
path('add_account/', views.add_new_supplier, name = 'addsupplier'),
path('analysis/', views.supplieritemalysis, name='supplieritemalysis'),

url(r'^edit_supplieritem/(?P<pk>\d+)' , views.edit_supplieritem, name='edit_supplieritem'),
url(r'^delete_supplieritem/(?P<pk>\d+)' , views.delete_supplieritem, name='delete_supplieritem'),
]