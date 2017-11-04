from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def account(request):
    return render(request, 'users/account.html', {'user': request.user})

def signup(request):
    if request.method == 'POST': 
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/account')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':    
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/account')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
