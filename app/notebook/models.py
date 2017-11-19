from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, default='', unique=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='Tag')
    title = models.CharField(max_length=255, default='')
    body = models.TextField(default='')
    date = models.DateTimeField()

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

