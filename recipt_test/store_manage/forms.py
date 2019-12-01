from django import forms
from .models import *

class Recipt_Form(forms.ModelForm):
    class Meta:
        model = Recipt
        fields = ['reciptName']

        labels = {
            'reciptName': "이 름 "
        }