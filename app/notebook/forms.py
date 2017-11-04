from django import forms
from datetime import datetime
from .models import *

class CreatePostForm(forms.Form):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'input'}))
    body = forms.CharField(label='Post', 
                           widget=forms.Textarea(attrs={'class': 'textarea'}))
    categories = forms.CharField(label='Tags',
                                 widget=forms.TextInput(attrs={'class': 'input'}))
    
    def save(self, request):
        title = self.cleaned_data['title']
        body = self.cleaned_data['body']
        post = Post.objects.create(user=request.user,
                           date=datetime.now(),
                           body=body,
                           title=title)
        return post
