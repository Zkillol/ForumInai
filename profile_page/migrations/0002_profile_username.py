# Generated by Django 4.2.7 on 2023-11-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
