from rest_framework import generics, permissions
from api.serializers.track_serializers import TrackSerializer,TrackListCreateSerializer
from music.models import Track


class TrackListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve and create tracks.
    """
    queryset = Track.objects.all()
    serializer_class = TrackListCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class TrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a track.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   