from django.db import models


class Posts(models.Model):
    title = models.CharField( 'Название',max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='media/posts/' , null=True)
    # likes = models.PositiveIntegerField()
    # comments = models.CharField('Написать комментарий ' ,max_length=250 )



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


