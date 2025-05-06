from typing import Any
from django.shortcuts import render
from .models import Track, Artist, Album
import random
from django.views.generic import DetailView
from django.db.models import Q


def home_view(request):
    trackset = Track.objects.all()
    albumset = Album.objects.all()
    tracklist = list(trackset)
    albumlist = list(albumset)
    random.shuffle(tracklist)
    shuffledTracklist = tracklist[:20]
    random.shuffle(albumlist)
    shuffledAlbum = albumlist[:20]
    data = {
        'tracks':shuffledTracklist,
        'albums': shuffledAlbum
    }
    return render(request, 'music/home.html',context=data)


def search_view(request):
    query = request.GET.get('q',None)
    if query is None:
        return render(request, 'music/search.html')
    else: 
        tracks = Track.objects.filter(
           Q(title__icontains=query)
        )
        albums = Album.objects.filter(
            Q(title__icontains=query)
        )
        artists = Artist.objects.filter(
            Q(name__icontains=query)
        )
        data={
            'query' : query,
            'tracks' : tracks,
            'albums':albums,
            'artists':artists
        }
    
        return render(request,'music/search.html',context=data) 

def songs_view(request):
    trackset = Track.objects.all()
    tracklist = list(trackset)
    random.shuffle(tracklist)
    quick_pick_tracklist = tracklist[:20]
    random.shuffle(tracklist)
    most_listening_tracklist = tracklist[:20]
    print('size is',len(quick_pick_tracklist))
    data = {
        'quick_picks':quick_pick_tracklist,
        'most_listening':most_listening_tracklist
    }
    return render(request, 'music/songs.html',context=data)

class TrackDetailView(DetailView):
    model = Track
    template_name = 'music/track_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Exclude the current track from the album's track list
        context['album_tracks'] = self.object.album.tracks.exclude(id=self.object.id)
        return context


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'music/album_detail.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["album_tracks"] = self.object.tracks.exclude(id=self.object.id)
        return context
    