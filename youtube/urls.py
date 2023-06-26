from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('upload/', UploadVideo.as_view(), name='upload'),
    path('video/<int:video_id>', VideoPlayer.as_view(), name='video'),
    path('search', SearchVideo.as_view(), name='search'),
    path('like_video/', like_video, name='like_video'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)