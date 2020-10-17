from django.shortcuts import render, redirect, get_object_or_404
from .forms import CalcForm
from .models import Account

# Create your views here.
def home(request):
    account = get_object_or_404( Account, pk=1)
    balance = account.balance
    context = { 'username': 'Ian Studmeyer', 'balance' : balance}
    return render( request, 'portfolio/home.html', context)

def calc(request):
    account = get_object_or_404( Account, pk=1)
    balance = account.balance
    if request.method == "POST":
        form = CalcForm( request.POST)
        if form.is_valid(): #look up error codes for is_valid option if else
            amount = form.cleaned_data['amount']
            action = request.POST['submit'] 
            if action == "Add": #note - will want to change to buy
                account.balance = balance + amount
            else:
                if amount <= balance:
                    account.balance = balance - amount
                else:
                    print('error: insufficient balance')
            account.save();
            return redirect('/')
    if request.method == "GET":
        form = CalcForm()
        context = { 'form': form}
        return render( request, 'portfolio/calc.html', context)