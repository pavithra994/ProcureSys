from django.db import models
from accounts.models import User

# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    is_ProcueStaff = models.BooleanField(default=False)
    is_HRStaff = models.BooleanField(default=False)
    is_DeliveryStaff = models.BooleanField(default=False)
    is_Accountant = models.BooleanField(default=False)
    is_SiteManager = models.BooleanField(default=False)
    is_Inspector = models.BooleanField(default=False)

