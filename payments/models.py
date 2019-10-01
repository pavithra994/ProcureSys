from django.db import models
from staff.models import Staff
from supplier.models import Supplier
from django.utils.timezone import datetime

# Create your models here.
class Payments(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now)
    amount = models.FloatField()
    accepted_by = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)
    done = models.BooleanField(default=False)

    def make_accept(self,staff):
        self.date = datetime.now
        self.accepted_by = staff

