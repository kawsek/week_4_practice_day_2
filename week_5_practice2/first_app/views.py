from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

@method_decorator(login_required, name = 'dispatch')
class CreateMusicianView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'createmusician.html'
    success_url = reverse_lazy('create_musician')

@method_decorator(login_required, name = 'dispatch')
class CreateAlbumView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'createalbum.html'
    success_url = reverse_lazy('create_album')
    
@method_decorator(login_required, name = 'dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profilepage')

@method_decorator(login_required, name = 'dispatch')
class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profilepage')

@method_decorator(login_required, name = 'dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('profilepage')
    pk_url_kwarg = 'id'


@login_required
def profile(request):
    data = models.Album.objects.all()
    return render(request, 'profile.html', {'data' : data })

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('loginpage')
        else:
            form = forms.RegisterForm()
        return render(request, 'register.html', {'form' : form})
    else:
        return redirect('profilepage')

class UserLogin(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profilepage')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Information incorrcet')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        

def user_logout(request):
    logout(request)
    return redirect('loginpage')

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = forms.UserChangeData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profilepage')
    else:
        form = forms.UserChangeData(instance = request.user)   
        return render(request, 'edit.html', {'form' : form})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profilepage')
    else:
        form = PasswordChangeForm(user= request.user)
        return render(request, 'pass_change.html', {'form' : form})
    