from django import forms

class CalcForm( forms.Form):
    amount = forms.IntegerField(initial=10) #can I pass database amount to there?