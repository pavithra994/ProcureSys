from django import forms
from order.models import *
from product.models import Product

class OrderPlacementForm(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    delivery_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your Content"}))
    class Meta:
        model = Order
        fields = ('company_name','delivery_address','description')

class AddTender(forms.ModelForm):
    products = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                         queryset=Product.objects.order_by('productType'),
                                         empty_label="(Select Product Type)")
    quantity = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter quantity'}))

    class Meta:
        model = Tender
        fields =('products','quantity')

class ProductRequestOrderForm(forms.ModelForm):
    class Meta:
        model = Product_OrderRequest
        fields = ['order_request','product','quantity']

TenderFormset = forms.inlineformset_factory(OrderRequest,Product_OrderRequest, form=ProductRequestOrderForm,extra=2)

