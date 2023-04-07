from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.BooleanField(default=False)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
