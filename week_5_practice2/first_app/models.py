from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
class Album(models.Model):
    album_name = models.CharField(max_length=20)
    album_release_date = models.DateField()
    rating = models.IntegerField()
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name
    
