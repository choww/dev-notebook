from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
import pdb

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
    tags = [tag.category.name for tag in post.tag_set.all()]
    form = EditPostForm(request.POST or None, 
                        instance=post,
                        initial={'categories': ','.join(tags) })
    if request.method == 'POST': 
        if form.is_valid():
            form.save(post)
            return redirect('/posts')
    return render(request, 'notebook/edit.html', {'form': form, 'pk': id})

@login_required
def destroy(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('/posts')
