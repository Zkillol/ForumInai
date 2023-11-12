# Generated by Django 4.2.7 on 2023-11-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='task',
            new_name='description',
        ),
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(null=True, upload_to='media/posts'),
        ),
    ]
