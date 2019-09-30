from django import forms
from order.models import *
from product.models import Product

class OrderPlacementForm(forms.ModelForm):
    product_and_quantity = forms.ModelMultipleChoiceField(queryset=Tender.objects.all(),widget=forms.CheckboxSelectMultiple)
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    supplier_name = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                           queryset=SupplierProductInfo.objects.order_by('supplier'),
                                           empty_label="(Select Supplier)")
    delivery_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    # quantity = forms.CharField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control'}))
    amount = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your Content"}))
    class Meta:
        model = Order
        fields = ('product_and_quantity','company_name','supplier_name' ,'delivery_address','amount', 'date', 'description')

class AddTender(forms.ModelForm):
    products = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                         queryset=Product.objects.order_by('productType'),
                                         empty_label="(Select Product Type)")
    quantity = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter quantity'}))

    class Meta:
        model = Tender
        fields =('products','quantity')

