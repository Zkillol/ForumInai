from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass




class Posts(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/posts')
    likes = models.PositiveIntegerField()
