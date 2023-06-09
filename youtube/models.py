from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    autor = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/%y')
    description = models.TextField(default='')
    preview = models.ImageField(upload_to='images/%y', default='/default_preview.jpg')
    likes = models.ManyToManyField(User, related_name='liked_videos')
    def __str__(self):
        return self.title

    def toggle_like(self, user):
        like, created = self.likes.get_or_create(user=user)
        if not created:
            like.delete()
        return like

    def like_count(self):
        return self.likes.count()

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exist()


class VideoLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='liked_videos')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'video')
