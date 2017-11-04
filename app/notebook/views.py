from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def create(request):
    if request.method == 'POST': 
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('/account')
    else: 
        form = CreatePostForm()
    return render(request, 'notebook/new.html', {'form': form}) 

@login_required
def index(request):
    return render(request, 
                  'notebook/index.html', 
                  {'posts': request.user.post_set.all() })
