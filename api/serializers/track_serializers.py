from rest_framework import serializers
from music.models import Track, Artist, Album


class TrackArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name','url']
        
class AlbumInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','title','cover_url','url']

class TrackSerializer(serializers.ModelSerializer):
    artists = TrackArtistInfoSerializer(many=True)
    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'cover_url','artists','url']
        
  
class TrackDetailSerializer(serializers.ModelSerializer):
    artists = TrackArtistInfoSerializer(many=True)
    album = AlbumInfoSerializer()
    class Meta:
        model = Track
        fields = ['id','title','duration','cover_url','artists','album','cover_url','audio_url','lyrics','url']


# This serializer is only for admin. It Creates, Updates, Deletes and List all Tracks.      
class TrackListCreateSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Artist.objects.all()
    )
    
    album = serializers.PrimaryKeyRelatedField(
        queryset = Album.objects.all()
    )
    
    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'release_date', 'cover_url', 'audio_url', 'lyrics', 'likes_count','album', 'artists']
        
        