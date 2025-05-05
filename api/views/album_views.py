from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers.album_serializers import AlbumSerializer, AlbumListCreateSerializer
from music.models import Album


class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]


class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumListCreateSerializer
    permission_classes = [IsAuthenticated]

    