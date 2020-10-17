from django import forms

class CalcForm( forms.Form):
    amount = forms.DecimalField(initial=10, max_digits=1000000, decimal_places=10) #can I pass database amount to there?