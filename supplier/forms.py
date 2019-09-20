from django import forms
from .models import *

class SupplierProductForm(forms.ModelForm):
    class Meta:
        model = SupplierProductInfo
        fields = ('Product_id', 'Product_Name', 'Supplier_Name', 'Qty', 'Amount')
