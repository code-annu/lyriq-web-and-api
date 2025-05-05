from rest_framework import serializers
from music.models import Artist
from .track_serializers import TrackDetailSerializer

class ArtistSerializer(serializers.ModelSerializer):
    tracks = TrackDetailSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id','name','gender','dob','img_url','tracks','albums']

class ArtistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


