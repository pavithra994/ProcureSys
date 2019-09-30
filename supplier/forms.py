from django import forms
from .models import *
from  product.models import Product

# class SupplierProductForm(forms.ModelForm):
#     class Meta:
#         model = SupplierProductInfo
#         fields = ('Product_type', 'Supplier_Name', 'Qty', 'Amount','Status')
#
#     def __init__(self, *args, **kwargs):
#         super(SupplierProductForm, self).__init__(*args, **kwargs)
#         instance = getattr(self, 'instance', None)
#         if instance and instance.id:
#             self.fields['Supplier_Name'].widget.attrs['readonly'] = True
# #

class SupplierProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     widget=forms.Select(
                                         attrs={
                                             'class': 'form-control',
                                             'autofocus': 'autofocus',

                                         }
                                     ),
                                     empty_label="(Select Product Type)")

    Qty = forms.IntegerField()
    Amount = forms.IntegerField()

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