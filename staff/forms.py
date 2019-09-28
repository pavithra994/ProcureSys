from django import forms


class AddStaffForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
                                                            attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',

                                                            }
                                                    ))
    full_name = forms.CharField(label='full_name', widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
        'autofocus': 'autofocus',

    }))

    is_ProcueStaff = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
                                                                                    'class': 'custom-control-input',
                                                                                    'id':'chkbox_horizontal1',
                                                                                }))
    is_HRStaff = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
                                                                                    'class': 'custom-control-input',
                                                                                    'id':'chkbox_horizontal2',
                                                                                }))
    is_DeliveryStaff = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
                                                                                    'class': 'custom-control-input',
                                                                                    'id':'chkbox_horizontal3',
                                                                                }))
    is_Accountant = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
                                                                                    'class': 'custom-control-input',
                                                                                    'id':'chkbox_horizontal4',
                                                                                }))
    is_SiteManager = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
                                                                                    'class': 'custom-control-input',
                                                                                    'id':'chkbox_horizontal5',
                                                                                }))
    is_Inspector =forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
                                                                                    'class': 'custom-control-input',
                                                                                    'id':'chkbox_horizontal6',
                                                                                }))
