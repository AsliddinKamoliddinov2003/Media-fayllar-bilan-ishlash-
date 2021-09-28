from os import truncate
from django.db import models
from django.db.models.fields import NullBooleanField


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(max_length=255)
    music = models.FileField(upload_to="music/", null=True)

    def __str__(self):
        return self.title
    

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="video/", null=True)

    def __str__(self):
        return self.title
