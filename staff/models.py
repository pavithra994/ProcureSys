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

    def get_position(self):
        position = ""
        if self.is_ProcueStaff:
            position += " Procurement Staff,"
        if self.is_HRStaff:
            position += " HR Staff,"
        if self.is_DeliveryStaff:
            position += " Delivery Staff,"
        if self.is_Accountant:
            position += " Accountant,"
        if self.is_SiteManager:
            position += " SiteManager,"
        if self.is_Inspector:
            position += " Inspector,"

        return position.rstrip(',').lstrip()

