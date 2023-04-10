from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user





class Video(models.Model):
    autor = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/%y')
    description = models.TextField(default='')
    preview = models.ImageField(upload_to='images/%y', default='/default_preview.jpg')
    def __str__(self):
        return self.title
