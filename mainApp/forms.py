from django import forms



class BasketAddProductForm(forms.Form):
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

    
