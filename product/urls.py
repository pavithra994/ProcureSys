from django.urls import path
from product import views
from django.conf.urls import url

urlpatterns =[
    path('',views.product_details, name='product_details'),
    # path('display/',views.displaySupplierProducts, name='displaySupplierProducts'),
    path('addProductType/', views.add_product_types, name='addProductType'),
    path('addProduct/', views.add_product, name='addProduct'),

    # url(r'^edit_supplieritem/(?P<pk>\d+)' , views.edit_supplieritem, name='edit_supplieritem'),
]