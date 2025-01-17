from django import forms
from utils.constants import COLOR_CHOICES


class BetForm(forms.Form):
    color = forms.ChoiceField(choices=COLOR_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control'}))
