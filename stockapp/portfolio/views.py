from django.shortcuts import render, redirect, get_object_or_404
from .forms import CalcForm

# Create your views here.
def home(request):
    context = { 'username': 'Ian Studmeyer'}
    return render( request, 'portfolio/home.html', context)

def calc(request):
    if request.method == "GET":
        form = CalcForm()
        context = { 'form': form}
        return render( request, 'portfolio/calc.html', context)