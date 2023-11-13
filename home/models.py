from django.db import models


class Posts(models.Model):
    title = models.CharField( 'Название',max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='posts/' , null=True)




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class LikesPost(models.Model):
    likes = models.PositiveIntegerField(null=False)

class CommentsPost(models.Model):
    comments = models.CharField('Написать комментарий ', max_length=250, null=True)