from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *

def signup(request):
    if request.method == 'POST': 
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':    
        form = LoginForm(data=request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/posts')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def account(request):   
    if request.user.is_authenticated: 
        return render(request, 'users/account.html', {'user': request.user})
    return redirect('/login')

@login_required
def edit(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditUserForm(None, instance=request.user)
    return render(request, 'users/edit.html', {'form': form})
