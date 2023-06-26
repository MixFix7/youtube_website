# Generated by Django 4.2 on 2023-05-12 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('youtube', '0009_remove_video_dislikes_remove_video_likes_video_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(related_name='liked_videos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='VideoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_videos', to='youtube.video')),
            ],
            options={
                'unique_together': {('user', 'video')},
            },
        ),
    ]
