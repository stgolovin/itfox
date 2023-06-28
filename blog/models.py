from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')


class Comment(models.Model):
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
