from django.shortcuts import render, redirect, get_object_or_404
from .forms import CalcForm
from .forms import MyAjaxForm 
from .models import Account
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def home(request):
    myajaxform = MyAjaxForm()
    account = get_object_or_404( Account, pk=1)
    balance = account.balance
    context = { 'myajaxform' : myajaxform, 'username': 'Ian Studmeyer', 'balance' : balance}
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

#for login
def handleAjax( request):
    name = request.POST['name'];
    print('name=' + name)
    return HttpResponse('hello ' + name)
def login_view( request):
    user = authenticate( request, username='root', password='root')
    if user is not None:
        print('username is authenticated')
        login( request, user)
        return redirect('/')
def logout_view( request):
    logout(request)
    return redirect('/')