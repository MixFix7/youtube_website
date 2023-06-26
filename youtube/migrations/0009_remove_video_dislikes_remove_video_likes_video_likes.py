# Generated by Django 4.2 on 2023-05-12 19:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('youtube', '0008_video_dislikes_video_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(related_name='video_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
