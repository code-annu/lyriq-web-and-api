from django.urls import path
from api.views.artist_views import *
from api.views.album_views import *
from api.views.track_views import *

urlpatterns = [
    # path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    # path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    # path('album/<str:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    # path('tracks/', TrackListCreateView.as_view(), name='track-list-create'),
    # path('track/<str:pk>/', TrackDetailView.as_view(), name='track-detail'),
    # path('artists/shuffle/',ArtistShuffleView.as_view(),name='artist-shuffle'),
    path('artists/<str:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
    path('artists/',ArtistShuffleView.as_view(),name='artist-shuffle'),
    path('artists/<str:pk>/albums',ArtistAlbumsView.as_view(),name='artist-albums'),
    path('search/artists/',ArtistSearchView.as_view(),name= 'search-artists'),
    path('albums/<str:pk>/',AlbumDetailView.as_view(),name='album-detail'),
    path('albums/',AlbumShuffleView.as_view(),name='albums-shuffle'),
    path('search/albums/',AlbumSearchView.as_view(),name='search-albums'),
    path('tracks/<str:pk>',TrackDetailView.as_view(),name='track-detail'),
    path('tracks/',TrackShuffleView.as_view(),name='tracks-shuffle'),
    path('search/tracks/',TrackSearchView.as_view(),name='search-tracks'),
    
    # Only admin can access these urls
    path('create_list/album/',AlbumListCreateView.as_view(),name='create-list-album'),
    path('operation/album/',AlbumRetrieveUpdateDestroyView.as_view(),name='operation-album'),
    path('create_list/track/',TrackListCreateView.as_view(),name='create-list-album'),
    path('operation/track/',TrackRetrieveUpdateDestroyView.as_view(),name='operation-album')

    
    
]
