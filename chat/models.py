from django.db import models
import profile
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profile_page.models import Profile


class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.user.username


class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_sender')
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_receiver')
    seen = models.BooleanField(default=False)


    def __str__(self):
        return self.body
