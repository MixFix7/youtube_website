from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Video
from .models import UserManager
from django.views import View
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse



class Home(ListView):
    model = Video
    template_name = 'youtube/index.html'

class VideoPlayer(View):
    def get(self, request, video_id):
        id = video_id
        all_videos = Video.objects.exclude(id=id)
        video = Video.objects.get(id=id)
        return render(request, template_name='youtube/video_player.html', context={'all_videos': all_videos, 'video': video})

def like_video(request):
    video_id = request.GET.get("id")
    video = Video.objects.get(pk=video_id)
    user = request.user

    if user.is_authencated:
        if user in video.likes.all():
            video.likes.remove(user)
        else:
            video.likes.add(user)

        return JsonResponse({'status': 'ok', 'likes': video.likes.count()})
    return JsonResponse({'status': 'error'})





class Register(TemplateView):
    template_name = 'youtube/register.html'

    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                password = password1
                user = User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Check your password")


class LoginPage(View):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user=user)
                return redirect('home')
            else:
                error = "Check your username or password"
                return render(request, 'youtube/login.html', {'username': username, 'password': password, 'error': error})

        return render(request, template_name='youtube/login.html')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')




class UploadVideo(View):
    def get(self, request):
        return render(request, template_name='youtube/upload.html')
    def post(self, request):
        if request.method == 'POST':
            video_file = request.FILES['video_file']
            title = request.POST['title']
            autor = request.POST['autor']
            description = request.POST['description']
            preview = request.FILES['preview']
            New_video = Video.objects.create(title=title, video_file=video_file, autor=autor, description=description, preview=preview)

            return redirect('home')

        return render(request, template_name='youtube/upload.html')

class SearchVideo(View):
    def post(self, request):
        if request.method == 'POST':
            value_search = request.POST['search_bar']
            search = Video.objects.filter(title__contains=value_search)
            return render(request, template_name="youtube/search.html", context={'search': search, 'value_search': value_search})
        else:
            return render(request, 'youtube/search.html')