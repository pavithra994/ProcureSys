from django.db import models
from supplier.models import SupplierProductInfo
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

class ProductType(models.Model):
    product_type = models.CharField(max_length=100)

    def __str__(self):
        return format(self.product_type)

class Product(models.Model):
    slug = models.SlugField(blank=True, unique=True)
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)
    price_per_product = models.FloatField()
    supplier = models.ForeignKey(SupplierProductInfo, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return format(self.slug)

class ProductOrder(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


def jewelry_presave_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(jewelry_presave_receiver, sender=Product)