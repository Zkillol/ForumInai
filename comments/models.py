from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from home.models import Posts
class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField('Комментарий')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Комментарий от {self.user.username} на пост '{self.post.title}'"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

