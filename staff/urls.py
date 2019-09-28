from django.urls import path
from .views import *


urlpatterns = [
    path('add_account/',create_new,name="create-staff"),
]