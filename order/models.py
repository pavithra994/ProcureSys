from django.db import models
from product.models import ProductType, ProductOrder
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
    slug = models.SlugField(blank=True, unique=True)
    product = models.ManyToManyField(Tender)
    amount = models.FloatField()
    date = models.DateField(default=datetime.now, blank=True)
    # description = models.CharField(max_length=500, blank=True)

    # if str(amount) > str(100000):
    #     Status = (
    #         ('Pending', 'Pending'),
    #         # ('Order Placed', 'Order Placed')
    #     )
    # else:
    #     Status = (
    #         # ('Pending', 'Pending'),
    #         ('Order Placed', 'Order Placed')
    #     )

    # def condition(self):
    #     if self.amount > 100000:
    #         return "Pending"
    #     else:
    #         return "Order Placed"

    Status = models.CharField(max_length=50, choices=Status, blank=True)

    def __str__(self):
        return format(self.slug)

    def get_tender_values(self):
        ret = ''
        print(self.product.all())

        for tend in self.product.all():
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