from django.db import models
from users.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()

