from django import forms
from .models import *

class SupplierProductForm(forms.ModelForm):
    class Meta:
        model = SupplierProductInfo
        fields = ('Product_type', 'Supplier_Name', 'Qty', 'Amount','Status')

    def __init__(self, *args, **kwargs):
        super(SupplierProductForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['Supplier_Name'].widget.attrs['readonly'] = True