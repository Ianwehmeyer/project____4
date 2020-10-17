from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home(request):
    context = { 'username': 'Ian Studmeyer'}
    return render( request, 'example/home.html', context)