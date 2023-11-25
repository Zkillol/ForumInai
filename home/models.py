from django.db import models
from django.utils import timezone
from django.conf import settings
from registration.models import User

class Posts(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, related_name="posts",
#         on_delete=models.DO_NOTHING, default=1
#     )
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='posts/', null=True)
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

