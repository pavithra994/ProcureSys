from django.urls import path
from order import views
from django.conf.urls import url

urlpatterns =[
    path('', views.display_order_request, name='display_order_request'),
    path('order_placement/', views.order_placement, name='order_placement'),
    # path('approval_request', views.approval_request, name='approval_request'),
    url(r'^approval_request/(?P<pk>\d+)', views.approval_request, name='approval_request'),
]