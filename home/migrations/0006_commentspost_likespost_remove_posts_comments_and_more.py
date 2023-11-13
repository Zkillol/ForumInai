# Generated by Django 4.2.7 on 2023-11-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_posts_comments_posts_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=250, null=True, verbose_name='Написать комментарий ')),
            ],
        ),
        migrations.CreateModel(
            name='LikesPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
    ]
