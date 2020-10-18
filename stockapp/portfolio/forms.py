from django import forms

class CalcForm( forms.Form):
    amount = forms.DecimalField(initial=10, max_digits=20, decimal_places=2) #can I pass database amount to there?

class AjaxForm( forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'name', 'placeholder': 'Enter a Name'}
    ))