from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Album)
admin.site.register(models.Musician)