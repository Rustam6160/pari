from django import forms
from .models import GoodDeed

class GoodDeedForm(forms.ModelForm):
    class Meta:
        model = GoodDeed
        fields = ['title', 'description']
