from os import name
from django.urls import path

from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("image/", image, name="image"),
    path("music/", music, name="music"),
    path("video/", video, name="video"),
]