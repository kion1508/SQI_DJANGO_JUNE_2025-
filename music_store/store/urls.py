from django.urls import path
from . import views
urlpatterns=[
    path('artist/',views.artist,name='artist'),
    path('album/',views.album,name='album'),
    path('home/',views.home,name='home'),
    path('song/',views.song,name='song'),
]