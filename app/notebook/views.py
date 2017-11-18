from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def create(request):
    if request.method == 'POST': 
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('/posts')
    else: 
        form = CreatePostForm()
    return render(request, 'notebook/new.html', {'form': form}) 

@login_required
def index(request):
    return render(request, 
                  'notebook/index.html', 
                  {'posts': request.user.post_set.all()})

@login_required
def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST': 
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('/posts')
    else: 
        form = EditPostForm(None, instance=post)
    return render(request, 'notebook/edit.html', {'form': form})
