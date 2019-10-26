from django import forms
from .models import *

class Store_Form(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['storeName']

        labels = {
            'storeName': '매장명'
        }