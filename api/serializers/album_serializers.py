from rest_framework import serializers
from music.models import Album
from .artist_serializers import ArtistSerializer
from music.models import Artist

class AlbumSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date','tracks_count', 'cover_url', 'artists','url']
        

class AlbumListCreateSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Artist.objects.all()
    )
    
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date','tracks_count', 'cover_url', 'artists','url']

        