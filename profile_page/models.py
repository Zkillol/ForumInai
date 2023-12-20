from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    id = models.AutoField(primary_key=True)
    date_modified = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    profile_bio = models.CharField(max_length=500, null=True)
    friends = models.ManyToManyField('chat.Friend', related_name='my_friends')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)