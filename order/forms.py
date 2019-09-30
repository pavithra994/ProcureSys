from django import forms
from order.models import *
from product.models import ProductType

class OrderPlacementForm(forms.ModelForm):
    product = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                        queryset=ProductType.objects.order_by('product_type'),
                                        empty_label="(Select Product Type)")
    quantity = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    amount = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your Content"}))
    class Meta:
        model = Order
        fields = ('product', 'quantity', 'amount', 'date', 'description')