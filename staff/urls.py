from django.urls import path
from .views import *


urlpatterns = [
    path('',staff_dashboard,name="staff_dashboard"),
    path('add_account/',create_new,name="create-staff"),
]