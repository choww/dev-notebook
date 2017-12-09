from django import forms
from datetime import datetime
from .models import *

class CreatePostForm(forms.Form):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'input'}))
    body = forms.CharField(label='Post', 
                           widget=forms.Textarea(attrs={'class': 'textarea'}))
    categories = forms.CharField(label='Tags (separate by commas)',
                                 widget=forms.TextInput(attrs={'class': 'input'}))
    
    def save(self, request):
        title = self.cleaned_data['title']
        body = self.cleaned_data['body']
        categories = self.cleaned_data['categories']
        post = Post.objects.create(user=request.user,
                           date=datetime.now(),
                           body=body,
                           title=title)

        for tag in categories.split(','):
            category = Category.objects.get_or_create(name=tag.strip())[0]
            Tag.objects.create(user=request.user, 
                               post=post, 
                               category=category)
        return post

class EditPostForm(forms.ModelForm):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'input'}))
    body = forms.CharField(label='Post', 
                           widget=forms.Textarea(attrs={'class': 'textarea'}))
    categories = forms.CharField(label='Tags (separate by commas)',
                                 widget=forms.TextInput(attrs={'class': 'input'}))
    
    class Meta: 
        model = Post
        fields = ('title', 'body', 'categories')

    def save(self, post):
        post.title = self.cleaned_data['title']
        post.body = self.cleaned_data['body']
        categories = self.cleaned_data['categories']
        post.save()
        for tag in categories.split(','):
            category = Category.objects.get_or_create(name=tag.strip())[0]
            Tag.objects.get_or_create(user=post.user, 
                                      post=post,
                                      category=category)
        return post
