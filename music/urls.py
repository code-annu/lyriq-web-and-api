from django.urls import path
from .views import *

app_name = 'music'

urlpatterns = [
    path('', home_view, name='home'),
    path('search/', search_view, name='search'),
    path('songs/', songs_view, name='songs'),
    path('track/<uuid:pk>',TrackDetailView.as_view(),name='track_detail'),
    path('albums/<uuid:pk>',AlbumDetailView.as_view(),name= 'album_detail')
]
