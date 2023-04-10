from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Video
from .models import UserManager

def home(request):
    all_videos = Video.objects.all()
    return render(request, template_name='youtube/index.html', context={'all_videos': all_videos})


def upload_video(request):
    return render(request, 'youtube/upload.html')

def video_player(request, video_id):
    id = video_id
    all_videos = Video.objects.exclude(id=id)
    video = Video.objects.get(id=id)
    return render(request, template_name='youtube/video_player.html', context={'all_videos': all_videos, 'video': video})


def register(request):
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


    return render(request, template_name='youtube/register.html')

def loginPage(request):
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


def logoutPage(request):
    logout(request)
    return redirect('home')



@ login_required
def upload_video(request):
    if request.method == 'POST':
        video_file = request.FILES['video_file']
        title = request.POST['title']
        autor = request.POST['autor']
        description = request.POST['description']
        preview = request.FILES['preview']
        New_video = Video.objects.create(title=title, video_file=video_file, autor=autor, description=description, preview=preview)

        return redirect('home')

    return render(request, template_name='youtube/upload.html')

def search_video(request):
    if request.method == 'POST':
        value_search = request.POST['search_bar']
        search = Video.objects.filter(title__contains=value_search)
        return render(request, template_name="youtube/search.html", context={'search': search, 'value_search': value_search})
    else:
        return render(request, 'youtube/search.html')