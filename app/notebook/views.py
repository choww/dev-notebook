from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .helpers import *

@login_required
def create(request):
    if request.method == 'POST': 
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('/'+request.user.username)
    else: 
        form = CreatePostForm()
    return render(request, 'notebook/new.html', 
                  {'form': form, 'tags': tags(request.user), 'user': request.user}) 

def index(request, username):
    user = User.objects.get(username=username)
    posts = user.post_set.all().order_by('-date')
    return render(request, 
                  'notebook/index.html', 
                  {'posts': posts, 'tags': tags(user), 'user': user})

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
            return redirect('/'+request.user.username)
    return render(request, 
                  'notebook/edit.html', 
                  {'form': form, 'pk': id, 'user': request.user})

@login_required
def tag(request, username, name):
    user = get_object_or_404(User, username=username)
    category = get_object_or_404(Category, name=name)
    tagged_posts = request.user.tag_set.filter(category_id=category.id).order_by('-post_id')
    return render(request, 
                  'tag/show.html', 
                  {'tagged_posts': tagged_posts, 'category': category, 'tags':  tags(user), 'user': user})

@login_required
def destroy(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('/'+request.user.username)
