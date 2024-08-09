from django.urls import path
from . import views

urlpatterns = [
    path('create_musician/', views.CreateMusicianView.as_view(), name = 'create_musician'),
    path('create_album/', views.CreateAlbumView.as_view(), name = 'create_album'),
    path('edit_album/<int:id>', views.EditAlbumView.as_view(), name = 'edit_album'),
    path('delete_album/<int:id>', views.DeleteAlbumView.as_view(), name = 'delete_album'),
    path('edit_musician/<int:id>', views.EditMusicianView.as_view(), name = 'edit_musician'),
    path('register/', views.register, name = 'registerpage'),
    path('login/', views.UserLogin.as_view(), name = 'loginpage'),
    path('logout/', views.user_logout, name = 'logoutpage'),
    path('profile/', views.profile, name = 'profilepage'),
    path('profile/edit_profile/', views.edit_profile, name = 'edit_profilepage'),
    path('profile/edit_profile/pass_change/', views.pass_change, name = 'pass_changepage'),
]