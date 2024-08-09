from django import forms 
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
class UserChangeData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',]


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"
class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = "__all__"