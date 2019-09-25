from django.db import models

# Create your models here.

class SupplierProductInfo(models.Model):
    Status = (
        ('Available', 'Available'),
        ('Less amount of Stock', 'Less Amount of Stock'),
        ('Out Of Stock', 'Out of Stock')
    )

    Product_id = models.CharField(max_length=6, blank=False,)
    Product_Name = models.CharField(max_length=100)
    Supplier_Name = models.CharField(max_length=100)
    Qty = models.IntegerField()
    Amount = models.CharField(max_length=50)
    Order_date = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=50, choices=Status, default='Available')

    def __str__(self):
        return 'Product_id: {0} Product_Name:{1} Supplier_Name:{2} Qty:{3}  Amount:{4} Order_date:{5} Status:{6}'.format(
            self.Product_id, self.Product_Name, self.Supplier_Name, self.Qty, self.Amount, self.Order_date, self.Status)