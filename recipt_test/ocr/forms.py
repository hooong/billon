from django import forms
from .models import *

class Recipt_imgForm(forms.ModelForm):
    class Meta:
        model = Recipt_img
        fields = ['recipt_img']

        labels = {
            'recipt_img': '영수증'
        }