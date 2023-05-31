# Django
from django import forms
# Models
from .models import *


class PQRForm(forms.ModelForm):
    """PQR Form"""
    request_type = forms.ChoiceField(choices=PQR.REQUEST_TYPE_CHOICES, label='Selecciona el tipo de solicitud')

    class Meta:
        model = PQR
        fields = ['request_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe tu solicitud aquí...'})
        }


class ProductForm(forms.ModelForm):
    """Product Form"""
    class Meta:
        model = Product
        exclude = ['category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['brand'].empty_label = 'Seleccione marca'
        self.fields['brand'].widget.attrs['class'] = 'form-control'

