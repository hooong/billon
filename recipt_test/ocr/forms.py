from django import forms
from .models import *

class Recipt_imgForm(forms.ModelForm):
    class Meta:
        model = Recipt_img
        fields = ['recipt_img_url']

        labels = {
            'recipt_img_url': '영수증'
        }