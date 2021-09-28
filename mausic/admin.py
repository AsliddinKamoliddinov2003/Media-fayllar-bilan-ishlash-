from django.contrib import admin
from django.db.models.base import Model
from django.db.models.fields.files import ImageField

from .models import  *


admin.site.register(Music)
admin.site.register(Image)
admin.site.register(Video)
