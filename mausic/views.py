from django.shortcuts import render


from .models import *


def index(request):
    return render(request, "index.html")


def image(request):
    images = Image.objects.all()
    context = {
        "images":images
    }
    return render(request, "images.html", context)


def music(request):
    musics = Music.objects.all()
    context = {
        "musics":musics
    }
    return render(request, "music.html", context)


def video(request):
    videos = Video.objects.all()
    context = {
        "videos":videos
    }
    return render(request, "video.html", context)
