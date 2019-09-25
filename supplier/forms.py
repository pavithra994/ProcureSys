from django import forms
from .models import *

class SupplierProductForm(forms.ModelForm):
    class Meta:
        model = SupplierProductInfo
        fields = ('Product_type', 'Supplier_Name', 'Qty', 'Amount','Status')
