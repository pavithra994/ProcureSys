from django import forms
from .models import *

class SupplierProductForm(forms.ModelForm):
    class Meta:
        model = SupplierProductInfo
        fields = ('Product_type', 'Supplier_Name', 'Qty', 'Amount','Status')


class AddSupplierForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
                                                            attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',

                                                            }
                                                    ))
    full_name = forms.CharField(label='full_name', widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',

                                                            }
                                                    ))
