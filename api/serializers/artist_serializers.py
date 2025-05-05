from rest_framework import serializers
from music.models import Artist
from .track_serializers import TrackDetailSerializer
from .album_serializers import AlbumSerializer

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name','gender','dob','img_url']


class ArtistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name','img_url','gender','dob','url']


class ArtistAlbumsSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)
    total = serializers.SerializerMethodField()
    class Meta:
        model = Artist
        fields = ['id','name','img_url','albums','total']
        
    def get_total(self,obj):
        return obj.albums.count()

        