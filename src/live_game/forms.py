from django import forms

class BetForm(forms.Form):
    COLOR_CHOICES = [
        ('color1', 'Color 1'),
        ('color2', 'Color 2'),
    ]
    color = forms.ChoiceField(choices=COLOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
