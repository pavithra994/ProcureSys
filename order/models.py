from django.db import models
from product.models import ProductType, ProductOrder
from supplier.models import SupplierProductInfo
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.timezone import datetime


class Tender(models.Model):
    products = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return 'Product: {0} Quantity:{1} '.format(self.products, self.quantity)


class Order(models.Model):
    Status = (
        ('Pending', 'Pending'),
        ('Order Placed', 'Order Placed')
    )
    Status2 = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('NOT', 'NOT')
    )
    slug = models.SlugField(blank=True, unique=True)
    product_and_quantity = models.ManyToManyField(Tender)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    supplier_name = models.ForeignKey(SupplierProductInfo, on_delete=models.CASCADE, null=True, blank=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)
    amount = models.FloatField()
    date = models.DateField(default=datetime.now, blank=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    Status = models.CharField(max_length=50, choices=Status, blank=True)
    approval = models.CharField(max_length=50, choices=Status2, default="Approved")

    def __str__(self):
        return format(self.slug)

    def get_tender_values(self):
        ret = ''
        print(self.product_and_quantity.all())

        for tend in self.product_and_quantity.all():
            ret = ret + str(tend.products) + ' : ' + str(tend.quantity) + " , "
        # remove the last ',' and return the value.
        return ret[:-1]


def order_presave_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(order_presave_receiver, sender=Order)


class OrderOne(models.Model):
    product = models.ManyToManyField(ProductOrder)
    amount = models.FloatField()


class Invoice(models.Model):
    Status2 = (
        ('Approved', 'Approved'),
        ('NOT', 'NOT'),
        ('Pending', 'Pending'),
    )
    order_id = models.CharField(max_length=50, blank=True)
    date = models.DateField(default=datetime.now, blank=True)
    amount_due = models.FloatField()
    approval = models.CharField(max_length=50, choices=Status2, default="Pending")

    def __str__(self):
        return 'Order ID: {0} Date:{1} Amount:{2} '.format(self.order_id, self.date, self.amount_due)
