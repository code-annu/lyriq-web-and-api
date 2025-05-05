from rest_framework import serializers
from music.models import Album
from music.models import Artist
from .track_serializers import TrackSerializer


class AlbumArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name','url']
        

class AlbumSerializer(serializers.ModelSerializer):
    artists = AlbumArtistInfoSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date','tracks_count', 'cover_url','artists','url']
        
        
class AlbumDetailSerializer(serializers.ModelSerializer):
    artists = AlbumArtistInfoSerializer(many=True)
    tracks= TrackSerializer(many = True)
    class Meta:
        model = Album
        fields = ['id','title','release_date','tracks_count','cover_url','artists','tracks','url']
        


#------ This serializer is only for Admin purpose -------------
class AlbumListCreateSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Artist.objects.all()
    )
    
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date','tracks_count', 'cover_url', 'artists','url']

        