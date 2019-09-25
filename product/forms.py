from django import forms
from product.models import *
from supplier.models import SupplierProductInfo

class AddProductTypeForm(forms.ModelForm):
    product_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter new product type'}))

    class Meta:
        model = ProductType
        fields = ['product_type']

class AddProductForm(forms.ModelForm):
    productType = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                        queryset=ProductType.objects.order_by('product_type'),
                                        empty_label="(Select Product Type)")
    supplier     = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                        queryset=SupplierProductInfo.objects.order_by('Supplier_Name'),
                                        empty_label="(Select Supplier)")
    price_per_product = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your Content"}))
    class Meta:
        model = Product
        fields = ('productType', 'price_per_product', 'supplier', 'description')