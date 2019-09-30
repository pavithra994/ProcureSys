from django.urls import path
from product import views
from django.conf.urls import url

urlpatterns =[
    path('',views.display_products, name='display_products'),
    # path('display/',views.displaySupplierProducts, name='displaySupplierProducts'),
    path('addProductType/', views.add_product_types, name='addProductType'),
    path('addProduct/', views.add_product, name='addProduct'),
    url(r'^editProduct/(?P<pk>\d+)', views.edit_product, name='edit_product'),
    url(r'^deleteProduct/(?P<pk>\d+)', views.delete_product, name='delete_product'),

]