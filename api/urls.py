from django.urls import path
from api.views.artist_views import *
from api.views.album_views import AlbumListCreateView, AlbumDetailView
from api.views.track_views import TrackListCreateView, TrackDetailView


urlpatterns = [
    # path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    # path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    # path('album/<str:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    # path('tracks/', TrackListCreateView.as_view(), name='track-list-create'),
    # path('track/<str:pk>/', TrackDetailView.as_view(), name='track-detail'),
    path('artist/<str:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
    path('artists/shuffle/',ArtistShuffleView.as_view(),name='artist-shuffle'),
]
