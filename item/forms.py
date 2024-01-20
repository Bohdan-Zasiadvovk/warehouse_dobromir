from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'measure', 'category']

    measure = forms.ChoiceField(choices=Item.MEASURE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=Item.CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
