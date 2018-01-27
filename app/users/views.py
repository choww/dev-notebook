from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from PIL import Image
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
            return redirect('/account')
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
            return redirect('/dashboard')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def dashboard(request):   
    if request.user.is_authenticated: 
        return render(request, 'users/dashboard.html', {'user': request.user})
    return redirect('/login')

@login_required
def show(request):
    #photo = get_object_or_404(Image, photo=request.user.profile.photo) 
    return render(request, 'users/show.html', {'user': request.user})

@login_required
@transaction.atomic
def edit(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        profile = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid() and profile.is_valid():
            form.save()
            profile.save(request.user)
            return redirect('/account')
    else:
        form = EditUserForm(None, instance=request.user)
        profile = ProfileForm(None, instance=request.user.profile)
    return render(request, 'users/edit.html', {'form': form, 'profile_form': profile })
