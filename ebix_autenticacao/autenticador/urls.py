from django.urls import path, include
from .views import MusicList, MusicListWithoutAuthentication, register, token, refresh_token, revoke_token

urlpatterns = [
    path('musics/', MusicList.as_view(), name='music-list'),
    path('musicsna/', MusicListWithoutAuthentication.as_view(), name='music-list'),
    path('register/', register),
    path('token/', token),
    path('token/refresh/', refresh_token),
    path('token/revoke/', revoke_token),
]