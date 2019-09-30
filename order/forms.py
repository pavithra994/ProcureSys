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

# class AddTender(forms.ModelForm):
#     product_type = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
#                                          queryset=ProductType.objects.order_by('product_type'),
#                                          empty_label="(Select Product Type)")
#     Qty = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter quantity'}))
#
#     class Meta:
#         model = TenderProduct
#         fields =('product_type','Qty')

# class OrderForm(forms.ModelForm):
#     # supplier_name = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
#     #                                      queryset=supplier_name.objects.order_by('supplier_name'),
#     #                                      empty_label="(Select Supplier name)")
#     company_name = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control'}))
#     supplier_name = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
#                                            queryset=SupplierProductInfo.objects.order_by('Supplier_Name'),
#                                            empty_label="(Select Supplier)")
#
#     delivery_address = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control'}))
#     product_Qty = forms.ModelMultipleChoiceField(queryset=TenderProduct.objects.all(),required=True,
#                                                 widget=forms.CheckboxSelectMultiple)
#
#     description = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control'}))
#     price = forms.CharField( widget=forms.NumberInput(attrs={'class':'form-control'}))
#     Status = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control'}))
#
#     class Meta:
#         model = OrderInfo
#         fields =( 'company_name','supplier_name','delivery_address', 'product_Qty', 'description', 'price', 'Status')
#         #exclude = ['order']