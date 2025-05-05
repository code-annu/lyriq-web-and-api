from rest_framework import serializers
from music.models import Track, Artist, Album

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'release_date', 'cover_url', 'audio_url', 'lyrics', 'likes_count','album', 'artists']
        
  
class TrackDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id','title','duration','cover_url']


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
        
        