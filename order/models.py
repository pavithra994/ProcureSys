from django.db import models
from product.models import ProductOrder, Product
from supplier.models import SupplierProductInfo, Supplier
from staff.models import Staff
from payments.models import Payments
from accounts.models import User
from staff.models import Staff
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.timezone import datetime


class Tender(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    site = models.ForeignKey(Staff,on_delete=models.CASCADE, null=True, default=None)
    proceed = models.BooleanField(default=False)


    def __str__(self):
        return 'Product: {0} Quantity:{1} '.format(self.products, self.quantity)

    def get_amount(self):
        return  self.products.price_per_product * self.quantity


class Order(models.Model):

    choices = (
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
        ('NOT', 'NOT')
    )
    slug = models.SlugField(blank=True, unique=True)
    product_and_quantity = models.ManyToManyField(Tender,blank=True)
    amount = models.FloatField(default=0)
    site = models.ForeignKey(Staff,on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=datetime.now, blank=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    Status = models.CharField(max_length=50, choices=choices, blank=True)

    def __str__(self):
        return format(self.slug)

    def mark_approved(self,approved_by = None):
        self.Status = 'Approved'
        for tender in self.product_and_quantity.all():
            supplier_product = SupplierProductInfo.objects.filter(product=tender.products)[0]
            payment = Payments(supplier=supplier_product.supplier,amount=tender.get_amount(),accepted_by=approved_by,done=True)
            payment.save()
            invoice = Invoice.objects.create(order=self,supplier_product=supplier_product,amount_due=tender.get_amount(),payment=payment)
            invoice.save()


    def set_status(self):
        if self.amount < 100000:
            self.mark_approved()
        else:
            self.Status = 'Pending'

class OrderRequest(models.Model):
    choices = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )
    status = models.CharField(max_length=63, choices=choices, default="Pending")
    date = models.DateTimeField(auto_now=True)
    total = models.FloatField(null=True)


class Product_OrderRequest(models.Model):
    order_request = models.ForeignKey(OrderRequest, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


def order_presave_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(order_presave_receiver, sender=Order)


class OrderOne(models.Model):
    product = models.ManyToManyField(ProductOrder)
    amount = models.FloatField()


class Invoice(models.Model):
    # Status2 = (
    #     ('Approved', 'Approved'),
    #     ('NOT', 'NOT'),
    #     ('Pending', 'Pending'),
    # )
    order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True)
    supplier_product = models.ForeignKey(SupplierProductInfo,on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.now, blank=True)
    payment = models.ForeignKey(Payments,on_delete=models.CASCADE, null=True)
    amount_due = models.FloatField(blank=True)
    # approval = models.CharField(max_length=50, choices=Status2, default="Pending")

    def __str__(self):
        return 'Order ID: {0} Date:{1} Amount:{2} '.format(self.order.pk, self.date, self.amount_due)



